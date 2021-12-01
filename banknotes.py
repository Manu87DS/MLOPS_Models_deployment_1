# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:19:16 2021

@author: utilisateur
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float