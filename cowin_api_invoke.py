# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:29:13 2021

@author: datascientistpur
"""

import os
import pickle
counter=0
os.system("""pip install -r requirements.txt""")

while 1==1:
    if counter>0:
        with open('test.pkl', 'rb') as f:
            data = pickle.load(f)
        print(data)
    else:
        counter+=1
    '''
    Arguments:
        1.District ID-If it is unknown then lookup the id master for the apt district and paste its id 
        2.Age
        3.Number of days to iterate for searching the vaccination availability
        4.From Email address
        5.To Email Address
        6.Email Password
        7.Time to halt before next iteration
        8. Mailing Activity[if 'y' or 'Y' then the entire list for the apt group containing free spots and date is mailed] else the details of  only those vaccination spots will be mailed that have free spots.
        
    '''
    os.system("""python cowin_api_fetch.py 294 8 19 abc@gmail.com xyz@gmail.com **** 120 y""")
    
    
