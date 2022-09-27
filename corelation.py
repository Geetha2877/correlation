import csv
import numpy as np
import plotly.express as px


def plotFigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Temperature",y="Icecream")
        fig.show()

def getDataSource(data_path):
    temperature=[]
    icecream= []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            icecream.append(float(row["Icecream"]))

    return {"x" : temperature, "y": icecream}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between temperature and icecream:-  \n--->",correlation[0,1])

data_path  = "icecreamdata.csv"
datasource=getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)
