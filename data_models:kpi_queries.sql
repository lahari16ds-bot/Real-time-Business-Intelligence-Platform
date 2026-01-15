-- Executive KPI Summary
SELECT
    kpi_name,
    AVG(kpi_value) AS avg_value,
    MAX(kpi_value) AS peak_value
FROM fact_kpi_metrics
WHERE kpi_timestamp >= DATEADD(hour, -24, GETDATE())
GROUP BY kpi_name;

-- Department performance
SELECT
    department,
    SUM(kpi_value) AS total_value
FROM fact_kpi_metrics
WHERE kpi_name = 'Revenue'
GROUP BY department;

-- Real-time refresh lag
SELECT
    MAX(kpi_timestamp) AS last_update,
    DATEDIFF(MINUTE, MAX(kpi_timestamp), GETDATE()) AS minutes_behind
FROM fact_kpi_metrics;
