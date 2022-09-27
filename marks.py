import csv
import numpy as np
import plotly.express as px


def plotFigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="days",y="marks")
        fig.show()

def getDataSource(data_path):
    days= []
    marks= []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days.append(float(row["days"]))
            marks.append(float(row["marks"]))

    return {"x" : days, "y": marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between days and marks:-  \n--->",correlation[0,1])

data_path  = "marksdata.csv"
datasource=getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)
