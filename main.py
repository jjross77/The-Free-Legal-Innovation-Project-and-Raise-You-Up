# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:53:57 2025

@author: yyyyyyyyyyyyyyyyyyyy
"""
from fastapi import FastAPI
app = FastAPI()
from psp_search_function_api_functions import search_functions
from psp_search_function_api_functions import search_functions_child
from psp_search_function_api_functions import search_functions_gchild
from psp_search_function_api_functions import search_functions_g2_child
search=search_functions()
search_c=search_functions_child()
search_g=search_functions_gchild()
search_g2=search_functions_g2_child()

from pydantic import BaseModel
import torch
from transformers import pipeline
import os
from accelerate import Accelerator
from fastapi import FastAPI, HTTPException
print('set up psp search api on big white in business fucntions under transfer_psp_search_function_api_to_big_white')

#import torch
# note guide in downloads called guide for huggingface to gety token to work
from transformers import pipeline
torch.backends.cuda.matmul.allow_tf32 = True
# Initialize Accelerator
accelerator = Accelerator(device_placement=True)
# Ensure you're using the CPU if no GPU is available
device = accelerator.device
print(f"Using device: {device}")
os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # or "0,1" for multiple GPUs
import torch
print(torch.cuda.is_available())  # Should be True if CUDA is available
print(torch.cuda.device_count())  # Number of GPUs available
model_id = "meta-llama/Llama-3.2-3B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
class psp_search(BaseModel):
      psp_search: str
      type_of_search: str
      positional_info_dic: str

      
      
class type_of_search(BaseModel):
      psp_search: str
      type_of_search: str
      positional_info_dic: str

      
class psp_search_item(BaseModel):
      psp_search: str
      type_of_search: str
      positional_info_dic: str
   #@app.post("/items/")
   #async def create_item(item: Item):
   #    return {"name": item.name, "price": item.price}
@app.get("/psp_search/")
#async def psp_search_function(skip: str,skip2: str):
#    print(skip)
async def psp_search_function(search: str, typee: str, positional_info_dic : str):
    try:
        #all_task_info_dict_list_dic=[search,"meow"]
        all_task_info_dict_list_dic=search_g2.add_strategy(search,typee,positional_info_dic,objective="helping the most people")
        #print(all_task_info_dict_list_dic)
    except Exception as E:
        print(E)
        return {"error":E}
 
    return {"all_task_info_dict_list_dic":all_task_info_dict_list_dic}
 #return {"name":outputs[0]["generated_text"][-1] , "price": price}
 #messages = [ {"role": "system", "content": f"{prompt}"}]

 #outputs = pipe(messages, max_new_tokens=500)
 #print(outputs[0]["generated_text"][-1])
