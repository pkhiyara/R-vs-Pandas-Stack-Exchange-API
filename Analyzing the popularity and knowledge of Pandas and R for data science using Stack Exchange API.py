# Import relevant packages
import pandas as pd
import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import json

# GET HTTP Requests for questions tagged as R and Pandas across the Stack Overflow subcommunity sorted by popularity
stackR = requests.get("https://api.stackexchange.com/2.2/tags/r/info?order=desc&sort=popular&site=stackoverflow")
stackP = requests.get("https://api.stackexchange.com/2.2/tags/pandas/info?order=desc&sort=popular&site=stackoverflow")

# GET HTTP Requests for questions tagged as R and Pandas across the Cross Validated subcommunity sorted by popularity
crossR = requests.get("https://api.stackexchange.com/2.2/tags/r/info?order=desc&sort=popular&site=stats")
crossP = requests.get("https://api.stackexchange.com/2.2/tags/pandas/info?order=desc&sort=popular&site=stats")

# GET HTTP Requests for questions tagged as R and Pandas across the Data Science subcommunity sorted by popularity
dataR = requests.get("https://api.stackexchange.com/2.2/tags/r/info?order=desc&sort=popular&site=datascience")
dataP = requests.get("https://api.stackexchange.com/2.2/tags/pandas/info?order=desc&sort=popular&site=datascience")

# Converting the results of the HTTP requests into JSON objects
stackRjson = stackR.json()
stackPjson = stackP.json()
crossRjson = crossR.json()
crossPjson = crossP.json()
dataRjson = dataR.json()
dataPjson = dataP.json()
stackRjson

# Normalize the JSON objects into individual dataframes
stackRdf = json_normalize(stackRjson["items"])
stackRcount = stackRdf["count"][0]
stackPdf = json_normalize(stackPjson["items"])
stackPcount = stackPdf["count"][0]
crossRdf = json_normalize(crossRjson["items"])
crossRcount = crossRdf["count"][0]
crossPdf = json_normalize(crossPjson["items"])
crossPcount = crossPdf["count"][0]
dataRdf = json_normalize(dataRjson["items"])
dataRcount = dataRdf["count"][0]
dataPdf = json_normalize(dataPjson["items"])
dataPcount = dataPdf["count"][0]

# Creating a summary dataframe that combines the number of tags for both data science tools across each of the three stack exchange subcommunities  
summarydf = pd.DataFrame({'Subcommunity': ["Stack Overflow", "Cross Validated", "Data Science", "All"], 'Number of Questions Tagged as R': [stackRcount, crossRcount, dataRcount, stackRcount+crossRcount+dataRcount], 'Number of Questions Tagged as Pandas': [stackPcount, crossPcount, dataPcount, stackPcount+crossPcount+dataPcount]})
summarydf

n_groups = 4
vals1 = summarydf["Number of Questions Tagged as R"]
vals2 = summarydf["Number of Questions Tagged as Pandas"]

# Create Barplot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rect1 = plt.bar(index, vals1, bar_width, alpha=opacity, color='b', label='R')

rect2 = plt.bar(index + bar_width, vals2, bar_width, alpha=opacity, color='g', label='Pandas')

plt.xlabel('Stack Exchange Subcommunities')
plt.ylabel('Number of Questions Tagged')
plt.title('Number of Questions Tagged by Data Science Tool based on Subcommunity')
plt.xticks(index + bar_width, ('Stack Overflow', 'Cross Validated', 'Data Science', 'All'))
plt.legend(loc='upper right', bbox_to_anchor=(1.25,1), title="Data Science Tool")
plt.rcParams["figure.figsize"] = [10, 6]
plt.tight_layout()
plt.show()
