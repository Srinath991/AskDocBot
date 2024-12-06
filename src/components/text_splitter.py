from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_data(doc,chunk_size,chunk_overlap,**kwargs):
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            **kwargs
        )
    return text_splitter.split_documents(doc)