import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from transformers import logging
logging.set_verbosity_error()
DOCUMENTS_FOLDER = "./documents"

class DocumentController:
    
    def __init__(self, documents_folder, model_name="BAAI/bge-small-en"):
        self.documents_folder = documents_folder
        self.embed_model = HuggingFaceEmbedding(model_name=model_name) 
        self.index = None

    def fetch_documents(self):
     
        if not os.path.exists(self.documents_folder):
            raise ValueError(f"Directory {self.documents_folder} does not exist. Please create it and add documents.")
        
        documents = SimpleDirectoryReader(self.documents_folder).load_data()
        if not documents:
            raise ValueError(f"No files found in {self.documents_folder}. Please add text or PDF files.")
        
        return documents

    def build_index(self):
    
        documents = self.fetch_documents()
        self.index = VectorStoreIndex.from_documents(documents, embedding=self.embed_model)  
        print("Successfull")
        return self.index

    def query_index(self, question):
        """
        Query the pre-built index to answer a given question.
        """
        if self.index is None:
            return "Error: Index is not initialized. Build the index first."
        
        try:
            response = self.index.query(question)
            return response.response
        except Exception as e:
            return f"Error querying index: {e}"
if __name__ == "__main__":
    controller = DocumentController(DOCUMENTS_FOLDER)
    try:
        print("Building the index...")
        controller.build_index()
        print("Index is ready for queries!")
    except ValueError as e:
        print(f"Failed to initialize: {e}")
        exit()
    while True:
        user_input = input("\nAsk a question (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        answer = controller.query_index(user_input)
        print(f"Answer: {answer}")
