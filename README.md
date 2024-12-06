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


## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Docker (for containerized deployment)
- Pinecone API Key
- Google Generative AI API Key
- LangChain API Key

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Srinath991/AskDocBot.git
   cd AskDocBot

2. Set up the environment variables: Create a .env file in the project root with the following content:
    PINECONE_API_KEY=<your_pinecone_api_key>
    PINECONE_ENV=<your_pinecone_environment>
    GOOGLE_API_KEY=<your_google_api_key>
    LANGCHAIN_API_KEY=<your_langchain_api_key>

3. Install dependencies:
    ```bash
   pip install -r requirements.txt

4. Run the FastAPI app:
    ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000

5. Access the web interface: Open http://localhost:8000 in your browser.

