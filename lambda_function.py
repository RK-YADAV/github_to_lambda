import json
import requests
import pandas as pd

def lambda_handler(event, context):
    # TODO implement

    print("Event Data -> ", event)
    response = requests.get("https://www.google.com")
    print("Google Se Yeh Aya - \n\n",response.text)

    # Example of using pandas
    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(d)
    print(df)

    print("Done x1.1")