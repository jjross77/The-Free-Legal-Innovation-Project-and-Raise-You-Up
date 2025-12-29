# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:04:48 2022

@author: yyyyyyyyyyyyyyyyyyyy
"""
import os

from pyspark.sql.types import *
from pyspark.ml import Pipeline
import sparknlp
from sparknlp import DocumentAssembler, Finisher
spark = sparknlp.start()


import sparknlp





 
space_path = os.path.join(r"D:\SCC", "test")
space = spark.sparkContext.wholeTextFiles(space_path)
schema = StructType([
 StructField('path', StringType()),
 StructField('text', StringType()),
])
space = spark.createDataFrame(space, schema=schema).persist()


#rows_w_indexed = space.rdd.zipWithIndex()

#indexed = rows_w_indexed.map(lambda row_index: Row(index=row_index[1], **row_index[0].asDict()))
#(i, path, text) = indexed.first()

#indexed_schema = schema.add(StructField('index', IntegerType()))
#indexed = spark.createDataFrame(indexed, schema=indexed_schema)\
# .persist()


assembler = DocumentAssembler()\
 .setInputCol('text')\
 .setOutputCol('document')
 


pipeline = Pipeline().setStages([
assembler]).fit(space)
indexed_w_tokens = pipeline.transform(space)
indexed_w_tokens.printSchema()

text, = indexed_w_tokens\
 .select("document" ).first()
text=str(text)


import nltk

from nltk.tokenize import sent_tokenize

test1=sent_tokenize(text)


import openpyxl


wb = openpyxl.load_workbook(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\sparrow_excelled.xlsx')
sheet = wb.active
Column_A = sheet['A'] 

dummy = 1

for i, sentence in enumerate(test1):
    dummy+= 1
    sheet[f'A{dummy}'] = sentence

wb.save(r"C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\sparrow_excelled.xlsx")












from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
model = AutoModel.from_pretrained("nlpaueb/legal-bert-base-uncased")

encoded_input = tokenizer(test1, return_tensors='pt', padding = True, truncation = True, max_length = 512)



import torch
with torch.no_grad():
     output = model(**encoded_input)
     print(output)

#for vector, sentnece in zip(X,test1):
#    cos_sim = dot(vector, vector2)/(norm(vector)*norm(vector2))

XX=output[1]
import numpy as np
from numpy import dot
from numpy.linalg import norm
X=np.array(XX)
cos_sim = dot(X[0], X[1])/(norm(X[0])*norm(X[1]))
print(cos_sim)