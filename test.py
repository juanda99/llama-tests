# load the large language model file
import datetime
from llama_cpp import Llama
LLM = Llama(model_path="./llama-2-7b-chat.ggmlv3.q4_0.bin")

# create a text prompt

print("*****************************************************************+")
prompt = "Q: What are the names of the days of the week? A:"
print(datetime.datetime.now())

def get_response(prompt):
    output = LLM(prompt)
    return output["choices"][0]["text"]

print(get_response(prompt))
# get time get_response execution

print(datetime.datetime.now())



