# 📚 DocuMind AI

An intelligent Retrieval-Augmented Generation (RAG) application that allows users to query documents, compare documents for contradictions, and receive grounded answers with citations using **Groq**, **ChromaDB**, and **FastAPI**.

---

## ✨ Features

* 📄 Supports PDF, Markdown, and Text documents
* ✂️ Intelligent document chunking
* 🔍 Semantic search using ChromaDB
* 🤖 Groq-powered LLM responses
* 📚 Source citations for every answer
* 🌍 Multilingual question support (English, Hindi, Marathi, etc.)
* ⚖️ Document contradiction detection
* 🚀 FastAPI REST API
* 🖥️ Streamlit web interface
* 🛡️ Hallucination protection using retrieval confidence

---

## 🏗️ Architecture

```text
Documents
     │
     ▼
Document Loader
     │
     ▼
Chunking Service
     │
     ▼
Embedding Model (BAAI/bge-m3)
     │
     ▼
ChromaDB Vector Store
     │
     ▼
Retriever
     │
     ▼
Prompt Builder
     │
     ▼
Groq LLM
     │
     ▼
Answer + Citations
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Streamlit
* LangChain
* ChromaDB
* Groq API
* HuggingFace Embeddings (BAAI/bge-m3)
* PyMuPDF
* Pydantic

---

## 📁 Project Structure

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
├── tests/
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/documind-ai.git
cd documind-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

---

## 🚀 Run the Backend

```bash
python -m uvicorn app.main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 🖥️ Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📡 API Endpoints

### Ask Questions

```
POST /ask
```

Example request:

```json
{
    "question": "What is FastAPI?"
}
```

---

### Compare Documents

```
POST /contradict
```

Example request:

```json
{
    "document_1":"fastapi.md",
    "document_2":"langchain.md",
    "topic":"API development"
}
```

---

## 🌍 Multilingual Support

Example:

**Question**

```
FastAPI क्या है?
```

**Answer**

```
फास्टएपीआई एक आधुनिक, तेज़ Python वेब फ्रेमवर्क है...
```

---

## 📚 Example Response

```json
{
  "answer": "...",
  "citations": [
    {
      "source": "fastapi.md",
      "page": 1,
      "chunk_id": 48
    }
  ]
}
```

---

## 📸 Screenshots

Add screenshots here after running the application:

* Streamlit Home
* Ask Question
* Document Comparison
* Swagger UI

---

## 🔮 Future Improvements

* Document upload from the UI
* Authentication
* Conversation history
* Hybrid search (keyword + vector)
* Docker support
* Cloud deployment
* OCR support for scanned PDFs

---

## 📄 License

This project is released under the MIT License.
