# 📚 DocuMind AI

> An end-to-end Retrieval-Augmented Generation (RAG) application that enables users to query documents, compare documents for contradictions, and receive grounded, citation-backed answers using **FastAPI**, **ChromaDB**, **Groq**, and **Streamlit**.

---

## 📑 Table of Contents

* Features
* Architecture
* Tech Stack
* Project Structure
* Installation
* How to Run
* API Endpoints
* Design Decisions
* Known Limitations
* Future Improvements
* AI Usage
* License

---

# ✨ Features

* 📄 Supports PDF, Markdown, and TXT documents
* ✂️ Intelligent document chunking
* 🔍 Semantic search using ChromaDB
* 🌍 Multilingual document retrieval
* 🤖 Groq-powered answer generation
* 📚 Source citations for every answer
* ⚖️ Document contradiction detection
* 🚀 FastAPI REST API
* 🖥️ Streamlit user interface
* 🛡️ Hallucination protection using retrieval confidence

---

# 🏗️ System Architecture

```text
                    Documents
         (PDF / Markdown / TXT)
                     │
                     ▼
             Document Loader
                     │
                     ▼
            Document Chunking
                     │
                     ▼
     HuggingFace Embeddings (BAAI/bge-m3)
                     │
                     ▼
           ChromaDB Vector Store
                     │
                     ▼
              Semantic Retriever
                     │
                     ▼
              Prompt Builder
                     │
                     ▼
             Groq Large Language Model
                     │
                     ▼
          Answer + Source Citations
```

---

# 🛠️ Tech Stack

| Component        | Technology              |
| ---------------- | ----------------------- |
| Language         | Python                  |
| Backend          | FastAPI                 |
| Frontend         | Streamlit               |
| LLM              | Groq                    |
| Embeddings       | HuggingFace BAAI/bge-m3 |
| Vector Database  | ChromaDB                |
| Framework        | LangChain               |
| Document Parsing | PyMuPDF, Unstructured   |
| Validation       | Pydantic                |

---

# 📁 Project Structure

```text
documind-ai/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── data/
│
├── tests/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/<your-username>/documind-ai.git

cd documind-ai
```

---

## Create a virtual environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

# ▶️ How to Run

## 1. Add documents

Place your PDF, Markdown, or TXT files inside the `data/` directory.

---

## 2. Build the vector database

```bash
python -m tests.test_ingest
```

This loads the documents, creates chunks, generates embeddings, and indexes them into ChromaDB.

---

## 3. Start the FastAPI backend

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 4. Launch the Streamlit interface

```bash
streamlit run streamlit_app.py
```

---

# 📡 API Endpoints

## Ask Questions

```
POST /ask
```

Example request

```json
{
    "question":"What is FastAPI?"
}
```

---

## Compare Documents

```
POST /contradict
```

Example request

```json
{
    "document_1":"fastapi.md",
    "document_2":"langchain.md",
    "topic":"API development"
}
```

---

# 🌍 Multilingual Support

Example:

Question

```
FastAPI क्या है?
```

Answer

```
फास्टएपीआई एक आधुनिक, तेज़ Python वेब फ्रेमवर्क है...
```

The application supports multilingual semantic retrieval using **BAAI/bge-m3** embeddings while maintaining citation-based responses.

---

# 📚 Example Response

```json
{
    "answer":"FastAPI is a modern, high-performance web framework for building APIs with Python.",
    "citations":[
        {
            "source":"fastapi.md",
            "page":1,
            "chunk_id":48
        }
    ]
}
```

---

# 🏗️ Design Decisions

Several architectural decisions were made to keep the application modular, maintainable, and easy to extend.

### Service-Oriented Design

Each responsibility is isolated into its own service (Loader, Chunker, Retriever, Prompt Builder, QA Service, LLM Service, and Vector Store Service). This reduces coupling and improves maintainability.

### Retrieval-Augmented Generation (RAG)

Instead of allowing the LLM to answer from its own knowledge, relevant document chunks are retrieved first and supplied as context. This improves factual grounding and reduces hallucinations.

### ChromaDB

ChromaDB was selected because it is lightweight, local, open-source, and integrates well with LangChain.

### BAAI/bge-m3 Embeddings

A multilingual embedding model was chosen to support semantic retrieval across English, Hindi, Marathi, and other languages.

### Groq LLM

Groq was selected due to its low latency and generous free developer tier, making it suitable for educational and portfolio projects.

### Citation-Based Responses

Every generated answer includes document citations (source, page, and chunk) so users can verify the information.

### Modular Backend

FastAPI exposes reusable REST endpoints while Streamlit acts purely as a frontend client. This separation makes future integrations easier.

---

# ⚠️ Known Limitations

The current implementation has the following limitations:

* Documents must be indexed before they become searchable.
* ChromaDB is configured for local storage only.
* OCR support for scanned PDFs is not implemented.
* User authentication is not available.
* Document upload from the web interface is not yet supported.
* The contradiction endpoint compares the most relevant retrieved chunks instead of complete documents.
* Large document collections may require additional optimization and background indexing.

---

# 🚀 Future Improvements

Planned enhancements include:

* Drag-and-drop document upload
* Automatic indexing after upload
* Authentication and user accounts
* Conversation history
* Memory-enabled chat
* Hybrid retrieval (keyword + semantic search)
* OCR support for scanned PDFs
* Docker support
* Cloud deployment
* Background indexing
* Retrieval evaluation metrics
* Better citation ranking and duplicate removal

---

# 💬 Code Documentation

Comments have been intentionally added only where implementation details are non-obvious, including:

* Retrieval logic
* Prompt construction
* Confidence threshold handling
* Vector store management
* Multilingual retrieval
* Contradiction detection workflow

Obvious Python syntax (such as loops or variable assignments) has intentionally not been commented to keep the code clean and readable.

---

# 🤖 AI Usage

AI tools were used as development assistants throughout this project. They supported development but did not replace implementation, debugging, or testing.

### AI-assisted tasks

* Brainstorming the overall RAG architecture
* Explaining FastAPI, LangChain, ChromaDB, and Groq concepts
* Assisting with Python code structure and refactoring
* Debugging runtime errors and dependency issues
* Improving prompts for retrieval and answer generation
* Suggesting software engineering best practices
* Assisting with project documentation

### Manual work

The following work was completed manually:

* Designing the application architecture
* Implementing the document ingestion pipeline
* Building the chunking and retrieval workflow
* Configuring ChromaDB indexing
* Integrating the Groq API
* Developing the FastAPI backend
* Developing the Streamlit frontend
* Testing API endpoints
* Debugging and validating application behavior
* Making implementation and architectural decisions

AI was used as a software development assistant, while all design decisions, integration, testing, debugging, and validation were performed by the project author.

---

# 📸 Screenshots

Add screenshots here after running the application.

Suggested screenshots:

* Streamlit Home
* Ask Question
* Multilingual Query
* Document Comparison
* Swagger UI

---

# AI Use Log

This project was developed with assistance from AI tools. AI was used to accelerate development, explain concepts, assist with debugging, and improve documentation. All architectural decisions, integration, implementation, testing, and validation were completed by the project author.

| AI Tool          | Approximate Usage | Purpose                                                                                                                                                                                                             |
| ---------------- | ----------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT (OpenAI) | ~50-150 messages | Discussed the RAG architecture, explained LangChain, ChromaDB, FastAPI, and Groq concepts, assisted with debugging, code refactoring, prompt engineering, multilingual support, API design, and README preparation. |

**Statement of honesty**

The AI assistant was used as a software engineering assistant to accelerate development and learning. Every generated suggestion was reviewed, integrated, modified where necessary, and tested before being included in the final implementation. All implementation decisions and final code validation were performed by the project author.
