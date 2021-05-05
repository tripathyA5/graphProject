import pandas as pd
import plotly_express as px 
df = pd.read_csv('covidData.csv')
fig = px.scatter(df,x="date", y="cases", color="country", title="Covid Data")
fig.show()