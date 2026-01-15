import pyodbc
import pandas as pd

df = pd.read_csv("live_kpis.csv")

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=BI;UID=sa;PWD=Password123")
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO fact_kpi_metrics (source_name, department, kpi_name, kpi_value, kpi_timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, row.source, row.department, row.kpi_name, row.kpi_value, row.kpi_timestamp)

conn.commit()
print("Data loaded into Synapse")
