-- Central KPI fact table for Power BI
CREATE TABLE fact_kpi_metrics (
    metric_id INT IDENTITY PRIMARY KEY,
    source_name VARCHAR(50),
    department VARCHAR(50),
    kpi_name VARCHAR(100),
    kpi_value FLOAT,
    kpi_timestamp DATETIME
);

-- Table to track data refresh & latency
CREATE TABLE pipeline_audit (
    run_id INT IDENTITY PRIMARY KEY,
    pipeline_name VARCHAR(50),
    start_time DATETIME,
    end_time DATETIME,
    rows_loaded INT,
    status VARCHAR(20)
);
