# -*- coding: utf-8 -*-
'''"IVC Ventures International Innovation Pvt Ltd (IVC Ventures) Confidential. 
    No license grant and not for distribution of any nature. All Rights Reserved."'''
def run_rag_pipeline(content_directory, model_name, model_url, query, similarity_top_k=4):
    
    import os
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
    from llama_index.llms.llama_cpp import LlamaCPP
    from llama_index.core.query_engine import RetrieverQueryEngine

    # Step 1: Create an embedding model
    embed_model = HuggingFaceEmbedding(model_name=model_name)

    # Step 2: Load documents and build the index
    if not os.path.exists(content_directory):
        raise FileNotFoundError(f"The directory '{content_directory}' does not exist.")
    
    documents = SimpleDirectoryReader(content_directory).load_data()
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

    # Step 3: Create a retriever
    retriever = index.as_retriever(similarity_top_k=similarity_top_k)
    query_engine = RetrieverQueryEngine(retriever=retriever)

    # Step 4: Define the LLM
    llm = LlamaCPP(
        model_url=model_url,
        temperature=0.1,
        max_new_tokens=256,
        context_window=3900,
        model_kwargs={"n_gpu_layers": 1},
        verbose=True,
    )

    # Step 5: Query the index and retrieve documents
    retrieved_docs = query_engine.query(query)

    # Step 6: Combine retrieved context with the query
    context = "\n".join(doc.text for doc in retrieved_docs.source_nodes)
    augmented_query = f"Context:\n{context}\n\nQuery:\n{query}"

    # Step 7: Generate a response from the LLM
    response = llm.complete(augmented_query)
    return response

# Example Usage
if __name__ == "__main__":
    content_dir = "content"
    embed_model_name = "BAAI/bge-small-en"
    llama_model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_0.gguf"
    user_query = "What does the box contain?"

    result = run_rag_pipeline(
        content_directory=content_dir,
        model_name=embed_model_name,
        model_url=llama_model_url,
        query=user_query
    )

    print("Generated Response:")
    print(result)
