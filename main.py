# this file is the main file of the project
from analyzer import analyze
from collector import collect_data
from anomaly_detector import detect_anomalies
def main():
    print("muon detector is starting...")
    collect_data()
    analyze()
    detect_anomalies()






main()