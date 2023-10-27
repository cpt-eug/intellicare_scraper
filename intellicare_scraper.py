import pandas as pd
import json

with open('./dentist.json', 'r') as file:
    data = json.load(file)

dentists = []

for i in data:
    dentists.append(i['value'])

df = pd.DataFrame(dentists)

df.to_csv('intellicare_dentists.csv')