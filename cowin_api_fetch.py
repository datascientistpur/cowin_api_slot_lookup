# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:13:14 2021

@author: Shravan
"""


'''
Load Libraries
'''
import requests
import datetime,time
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import pickle
import sys



def cowin_api_call(URL,id,numdays,age,from_user_id,to_user_id,email_password,sleep_secs=120,mailing_activity='N'):
       
    
    
    
    '''
    Date-Set for API Fetch
    '''
    start_date = datetime.datetime.today()
    date_list = [start_date + datetime.timedelta(days=x) for x in range(numdays)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]
    available=pd.DataFrame()
    
    '''
    Data Fetch
    '''
    for curr_date in date_str:
        
        URL = URL.format(id, curr_date)
        
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        cowin_response = requests.get(URL, headers=headers)
        #print(response)
        counter=0
        
        if cowin_response.ok:
            cowin_json = cowin_response.json()
            with open('test.pkl', 'wb') as f:
                pickle.dump(cowin_json, f)
            # print(json.dumps(resp_json, indent = 1))
            if cowin_json["centers"]:
                for center in cowin_json["centers"]:
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= age:
                            if mailing_activity=='Y' or mailing_activity=='y':
                                    tmp=pd.DataFrame({'center':[ center["name"]],'capacity':[session["available_capacity"]],'date':[curr_date]})
                                    available=pd.concat([available,tmp])
                                    counter+=1
                            elif( session["available_capacity"]>0):
                                counter+=1
                                tmp=pd.DataFrame({'center':[ center["name"]],'capacity':[session["available_capacity"]],'date':[curr_date]})
                                
                                if len(available)>0:
                                    available=pd.concat([available,tmp])
                                    
                                else:
                                    available=tmp
                                    
                            

    
    '''
    Mailing Activity
    '''
    
        
    if counter>0:
        s = smtplib.SMTP('smtp.gmail.com', 587)
      
        
        s.starttls()
      
      
        s.login(from_user_id, email_password)
      
       
        msg = MIMEMultipart()
        msg['Subject'] = "Vaccine"
        msg['From'] = from_user_id
        msg['To'] = to_user_id
        available=available.reset_index()
        html = """\
            <html>
            <head></head>
            <body>
            {0}
            </body>
            </html>
            """.format(available.to_html())
    
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
      
        
        
        s.sendmail(msg['From'],msg['To'], msg.as_string())
      
        
        s.quit()
        
    time.sleep(sleep_secs)



id=int(sys.argv[1])
numdays=int(sys.argv[2])
age=int(sys.argv[3])
from_id=sys.argv[4]
to_id=sys.argv[5]
email_pwd=sys.argv[6]
every_secs=int(sys.argv[7])
mailing_activity=sys.argv[8]

cowin_api_call('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}',id=id,numdays=numdays,age=age,from_user_id=from_id,to_user_id=to_id,email_password=email_pwd,sleep_secs=every_secs,mailing_activity=mailing_activity)

    