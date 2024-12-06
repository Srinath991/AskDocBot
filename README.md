# Document Q&A System

## 📜 Project Overview
The Document Q&A System enables users to upload documents (PDF or text), ask questions related to the document, and receive AI-generated answers in real-time. This project utilizes Google Generative AI for natural language processing, Pinecone for scalable vector storage, and LangChain to integrate retrieval-augmented generation (RAG). The system features a sleek, chatbot-style UI that enhances user interaction, making it a powerful tool for document-based queries.

## 🌟 Key Features
- **Document Upload**: Users can upload PDF or text files for processing.
- **Real-Time Q&A**: Users can ask questions related to the uploaded documents and receive instant, AI-powered answers.
- **Google Generative AI**: Utilizes embedding-001 for document embeddings and language understanding.
- **Pinecone Integration**: Pinecone handles document embeddings and allows efficient similarity search.
- **Chatbot-style UI**: A modern and interactive user interface for seamless user experience.
- **Containerization**: The project is containerized using Docker for easy deployment.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, LangChain, Pinecone, Google Generative AI
- **Frontend**: HTML, CSS, JavaScript (Interactive UI)
- **Database**: Pinecone (Vector database for search and retrieval)
- **Deployment**: Docker, AWS (Cloud deployment)
- **Others**: Uvicorn, Jinja2 templates for dynamic pages

## 📂 Project Structure
project/
├── app/
│   ├── main.py                 # FastAPI entry point
│   ├── routes.py               # API routes
│   ├── static/                 # Static files (CSS, JS)
│   ├── templates/              # HTML templates
│   ├── __init__.py
│   └── dependencies.py         # Dependency management
├── src/
│   ├── components/             # Core components for LLMs and embeddings
│   ├── pipelines/              # Document processing and query handling
│   ├── exception.py            # Custom exceptions
│   ├── logger.py               # Logging configuration
│   └── utils.py                # Utility functions
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # Project documentation
└── .env                        # Environment variables
