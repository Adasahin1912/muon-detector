import serial
import csv
import os

def collect_data():
    print("collecting data...")
    x = b"45231,3,18.0\r\n"
    x = x.decode("utf-8")
    parts =x.split(",")
    arduino_ms=float(parts[0])
    count=float(parts[1])
    cpm=float(parts[2])




    print(arduino_ms)
    print(count)
    print(cpm)
    file_exists = os.path.exists("readings.csv")
    with open("readings.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["arduino_ms", "count", "cpm"])
        writer.writerow([arduino_ms, count, cpm])


