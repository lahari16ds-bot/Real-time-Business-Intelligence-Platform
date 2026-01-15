import requests
import pandas as pd
from datetime import datetime

API_URL = "https://api.mockcompany.com/kpis"

def get_kpis():
    response = requests.get(API_URL)
    data = response.json()

    df = pd.DataFrame(data)
    df["kpi_timestamp"] = datetime.utcnow()
    return df

df = get_kpis()
df.to_csv("live_kpis.csv", index=False)
print("API data pulled successfully")
