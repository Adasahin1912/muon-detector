import pandas as pd
from sklearn.ensemble import IsolationForest
def detect_anomalies():
    print("anomaly detection is starting...")
    data2=pd.read_csv("readings.csv")
    print(data2)
    model = IsolationForest()
    model.fit(data2[["cpm"]])
    prediction= model.predict(data2[["cpm"]])
    print(prediction)
    data2["prediction"] = prediction
    print(data2)
    anomalies = data2[data2["prediction"] == -1]
    print("Anomalies:")
    print(anomalies)