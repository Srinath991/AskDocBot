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


### 🔍 How the System Works
1. Document Upload:
    - The user uploads a document via the web interface (PDF or TXT format).  
    The document is processed, and embeddings are created using Google Generative AI.  

2. Document Storage:
    - Embeddings are stored in Pinecone, which enables fast similarity search.

3. User Query:
    - The user asks a question related to the document.  
    The system retrieves relevant content from Pinecone and generates an answer using Google Generative AI.  

4. 📚 Use Cases
    - Legal: Automate document review and question answering for contracts, laws, etc.

    - Healthcare: Answer patient queries based on medical reports or research papers.

    - Education: Provide personalized answers to students based on educational materials.

### 🐳 Docker Deployment
    To deploy the application using Docker:

1. Build the Docker image:
    ```bash
    docker build -t document-qa .  
2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 --env-file .env document-qa  

Access the app: Open http://localhost:8000 in your browser.



Contributions are welcome! Please feel free to open issues or submit pull requests.

## 📝 License
    This project is licensed under the SrinathPromax License.


Feel free to further customize or add any additional sections as needed!
