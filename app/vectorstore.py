from langchain_chroma import Chroma
from app.embeddings import embedding_model

DB_PATH = "chroma_db"

vectorstore = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding_model,
    collection_name="documents"
)