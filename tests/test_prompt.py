from app.services.prompt_builder import PromptBuilder
from app.services.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What is FastAPI?"
)

prompt = PromptBuilder.build(
    "What is FastAPI?",
    results,
)

print(prompt)