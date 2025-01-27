from pathlib import Path

import sys
import logging
import os

from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts.prompts import SimpleInputPrompt
from llama_index.core import Settings
Settings.llm = None
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext, load_index_from_storage, StorageContext

storage_path = "storage/"

docs_path="docs"

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    #max_chunk_overlap = 20
    chunk_overlap_ratio = 0.1
    chunk_size_limit = 600

    #prompt_helper = PromptHelper(max_input_size, num_outputs, chunk_overlap_ratio, chunk_size_limit=chunk_size_limit)

    system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
    - StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
    - StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
    - StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
    - StableLM will refuse to participate in anything that could harm a human.
    """

    # This will wrap the default prompts that are internal to llama-index
    query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")


    llm = HuggingFaceLLM(
        context_window=4096,
        max_new_tokens=256,
        generate_kwargs={"temperature": 0.7, "do_sample": False},
        system_prompt=system_prompt,
        query_wrapper_prompt=query_wrapper_prompt,
        tokenizer_name="StabilityAI/stablelm-tuned-alpha-3b",
        model_name="StabilityAI/stablelm-tuned-alpha-3b",
        device_map="auto",
        stopping_ids=[50278, 50279, 50277, 1, 0],
        tokenizer_kwargs={"max_length": 4096},
        # uncomment this if using CUDA to reduce memory usage
        # model_kwargs={"torch_dtype": torch.float16}
    )
    #llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs)
    #llm_predictor = LLMPredictor(llm=llm)
    service_context = ServiceContext.from_defaults(chunk_size=1024, llm=llm, embed_model="local")
    


    documents = SimpleDirectoryReader(directory_path).load_data()

    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    #index = VectorStoreIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.storage_context.persist(persist_dir=storage_path)

    return index

def chatbot(input_text):
    index = load_index_from_storage(StorageContext.from_defaults(persist_dir=storage_path))
    #index = GPTVectorStoreIndex.load_from_disk('index.json')
    #query_engine = index.as_query_engine(response_synthesizer=response_synthesizer);
    query_engine = index.as_query_engine(streaming=True)

    response = query_engine.query(input_text)

    print(response.source_nodes)

    relevant_files=[]

    for node_with_score in response.source_nodes:
        print(node_with_score)
        print(node_with_score.node)
        print(node_with_score.node.metadata)
        print(node_with_score.node.metadata['file_name'])

        file = node_with_score.node.metadata['file_name']
        print( file )

        # Resolve the full file path for the downloading
        full_file_path = Path( docs_path, file ).resolve()

        # See if it's already in the array
        if full_file_path not in relevant_files:
            relevant_files.append( full_file_path ) # Add it

    print( relevant_files )

    return response.get_response(), relevant_files


index = construct_index(docs_path)
