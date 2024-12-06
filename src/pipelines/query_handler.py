from src.components.llms import get_google_llm
from src.components.embeddings import get_embeddings
from src.components.vector_store import get_pinecone_vector_store
from src.exception import CustomException
from src.logger import logging
import sys
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def handle_query(query,index_name):
    try:
        logging.info("Loading RAG prompt from LangChain Hub...")
        prompt = hub.pull("rlm/rag-prompt")
        
        logging.info("Initializing embeddings...")
        embeddings = get_embeddings()
        
        logging.info("Setting up LLM...")
        llm = get_google_llm()
        
        logging.info("Connecting to Pinecone vector store...")
        vector_store = get_pinecone_vector_store(index_name, embeddings)
        retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k": 1, "score_threshold": 0.5},
        )
        
        def format_docs(docs):
            """Format documents into a single string."""
            return "\n\n".join(doc.page_content for doc in docs)
        
        logging.info("Setting up RAG chain...")
        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        
        logging.info("Invoking the RAG chain...")
        result = rag_chain.invoke(query)
        return result
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise CustomException(e, sys)
