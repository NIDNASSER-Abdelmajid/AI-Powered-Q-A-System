from fastapi import FastAPI, Query
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub

app = FastAPI()

documents = []
VECTOR_DB_PATH = "faiss_index"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "HuggingFaceH4/zephyr-7b-alpha"
huggingfacehub_api_token = "" #Add huggingface api token

def load_and_index_documents():
    global documents
    pdf_loader = PyPDFLoader("data/example.pdf")
    text_loader = TextLoader("data/example.txt")
    documents = pdf_loader.load() + text_loader.load()
    documents = text_loader.load()
    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vector_db = FAISS.from_documents(documents, embedding_model)
    vector_db.save_local(VECTOR_DB_PATH)

load_and_index_documents()
embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
vector_db = FAISS.load_local(VECTOR_DB_PATH, embedding_model, allow_dangerous_deserialization=True)
llm = HuggingFaceHub(repo_id=LLM_MODEL, model_kwargs={"temperature": 0.1}, huggingfacehub_api_token=huggingfacehub_api_token)

# Create a custom prompt template
prompt_template = """
Context: {context}
Question: {question}
Provide only a direct answer to the question without any additional explanation or context.
Direct answer:"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_db.as_retriever(),
    chain_type_kwargs={
        "prompt": PROMPT
    },
    return_source_documents=False
)

@app.get("/ask")
async def ask_question(query: str = Query(..., title="Question")):
    try:
        answer = qa_chain.run(query)
        # Clean up the response
        answer = answer.split("Direct answer:")[-1].strip()
        answer = answer.split("\n")[0].strip()
        return answer
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)