from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings

embedding_model = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)