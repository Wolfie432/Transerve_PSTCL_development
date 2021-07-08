from flask import Flask
import requests
import pandas as pd
import json
from flask import make_response
#from data import funct

app=Flask(__name__)

@app.route('/',methods=['GET'])
def api():
    response = requests.get("https://tosapi.transerve.com/api/v2/public/attribute-info/6065b1188066f700252ed176?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNjA2NTkzZDkxNzA2MzYwMDFlM2U0NGY0Iiwic2Vzc2lvbiI6IjYwNjU5NmVhNTgyNjFlMDA1ZDU2MmRhMiIsImlhdCI6MTYxNzI3NzIwOH0.4dyjn87WR01AtGkrRmNoX3FIW0XbKT6cQ5I_cgUw0XU&layer_id=null&property=null&attribute=true")
    response_2=response.json()
    # converting json dataset from dictionary to dataframe
    train = pd.DataFrame.from_dict(response_2, orient='columns')
    train.reset_index(level=0, inplace=True)
    yellow=train.at[0,"layer_attribute_data"]
    green=pd.DataFrame.from_dict(yellow, orient='index').transpose()
    red=green.at[0,"attribute_data"]
    df = pd.DataFrame(red)
    df1=pd.DataFrame.from_records(df["properties"].values)
    resp = make_response(df1.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp