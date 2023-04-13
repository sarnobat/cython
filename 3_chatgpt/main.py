# from gpt_index import SimpleDirectoryReader,GPTListIndex,GPTSimpleVectorIndex,LLMPredictor,PromptHelper
from llama_index import SimpleDirectoryReader,GPTListIndex,GPTSimpleVectorIndex,LLMPredictor,PromptHelper

from langchain import OpenAI
import sys
import os

# os.environ["OPENAI_API_KEY"] = "foobar"

max_input = 4096
tokens = 200
chunk_size = 600 #for LLM, we need to define chunk size
max_chunk_overlap = 20

#define prompt
promptHelper = PromptHelper(max_input,tokens,max_chunk_overlap,chunk_size_limit=chunk_size)

#define LLM — there could be many models we can use, but in this example, let’s go with OpenAI model
llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001",max_tokens=tokens))

#load data — it will take all the .txtx files, if there are more than 1
# docs = SimpleDirectoryReader("/Volumes/git/repos_personal.git/mwk.git/snippets/programming_tips/sysadmin").load_data()
docs = SimpleDirectoryReader('/Volumes/git/repos_personal.git/mwk.git/snippets/programming_tips/sysadmin').load_data()


#create vector index
# vectorIndex = GPTSimpleVectorIndex(documents=docs,llm_predictor=llmPredictor,prompt_helper=promptHelper)
vectorIndex = GPTSimpleVectorIndex.from_documents(docs)

vectorIndex.save_to_disk("vectorIndex.json")

vIndex = GPTSimpleVectorIndex.load_from_disk("vectorIndex.json")
while True:
	question = input("Please ask: ")
	response = vIndex.query(question,response_mode="compact")
	print(f"Response: {response} \n")
