# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:46:01 2021

exemple pour débuter: https://anderfernandez.com/en/blog/how-to-create-api-python/

"""
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
app = FastAPI()
import pandas as pd
import pprint
# path ='xxxxxx'
data = pd.read_csv('questions.csv')
data = data.fillna('') # SOLVING BUG_1 : ValueError: Out of range float values are not JSON compliant

@app.get("/get_data")
def get_data():
    return data

##### l'utilisateur doit pouvoir choisir un type de test (use) ainsi qu'une ou plusieurs catégories (subject)
##### De plus, l'application peut produire des QCMs de 5, 10 ou 20 questions

from itertools import groupby
# data.sort(key=lambda content: content['use'])

# data2 = groupby(data, lambda x : x['use']) # pb avec les indices en str !!!!

# https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby

@app.get("/get_type_test")
async def get_type_test ():  
    # return data['use'].unique()                   #Internal Server Error
    
    ## values = set()
    ## for item in data:
        ## values.add(item['use'])
    ## values = set([i['use'] for i in data])
    ## return values                               #Internal Server Error
    
   #return data['use'][0]   # OK, affiche la 1ere ligne de la colonne use mais ce n'est pas ce que lon veut
   
   return  data #data2



# Declare function to return the sorted data based on name
@app.get("/get_type_test2")
async def get_type_test2 (data):
    # pprint.pprint(sorted(data, key=sort_by_key))
    return(sorted(data, key=sort_by_key))



#################################
class DATA (BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    responseA: str
    responseB: str
    responseC: str
    responseD: str
#################################

@app.post("/implement_new_data")
async def implement_new_data(answer: DATA):
    answer_dict = jsonable_encoder(answer)
    for key, value in answer_dict.items():
        answer_dict[key] = [value]
        answer_dict = {k:[v] for (k,v) in jsonable_encoder(answer).items()}
    return answer_dict