import pandas as pd
import matplotlib.pyplot as plt
def analyze():
    print("analyzing...")
    data=pd.read_csv("readings.csv")
    print(data)
    """plt.plot(data["cpm"])
    plt.show()"""

