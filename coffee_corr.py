import plotly.express as px
import csv

with open("coffeedata.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Coffee",y="sleep",color="week")
    fig.show()
