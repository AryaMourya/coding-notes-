import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('C:\Users\lenovo\coding-notes-\python notes\matplotlib\data.csv')
ids = data['Responder_id']
lang_responses = data['Responder_id']

Language_counter = Counter()

for response in lang_responses:
        Language_counter.update(response['LanguagesWorkedWith'].split(';'))



Languages = []
popularity = []

for item in Language_counter.most_common(15):
    Languages.append(item[0])
    popularity.append(item[1])

print(Languages)
print(popularity)

Languages.reverse()
popularity.reverse()

plt.barh(Languages,popularity)

plt.title("Most popular Languages")

plt.xlabel("User")

plt.tight_layout()

plt.show()

