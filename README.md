# Stack Exchange Popularity Analysis: R vs Pandas
A Python data manipulation and analysis project that examines and visualizes the popularity of widely used data science tools R and Pandas across 3 Stack Exchange subcommunities (Stack Overflow, Cross Validated, Data Science) through the use of the Stack Exchange API and multiple Python libraries such as Pandas, JSON, Requests, and Matplotlib.

## Methodology

Using the Stack Exchange API, GET HTTP requests were made for questions tagged as R and Pandas sorted by popularity across the Stack Overflow, Cross Validated, and Data Science subcommunities. The results of the HTTP requests were converted into JSON objects which were later normalized into individual dataframes for each subcommunity. Afterwards, a summary dataframe that combines the number of tags for both R and Pandas across each of the three Stack Exchange subcommunities was created and visualized as a barplot using the Matplotlib library.

## Results

![R vs Pandas Popularity Graph](/Stack_Exchange_Popularity_Graph.png)
