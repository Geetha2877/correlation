import plotly.express as px
import csv

with open("icecreamdata.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Temperature",y="Icecream")
    fig.show()
