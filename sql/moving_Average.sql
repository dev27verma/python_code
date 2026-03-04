| store_id | trans_date | total_sales |
| -------- | ---------- | ----------- |
| 101      | 2026-03-01 | 1000        |
| 101      | 2026-03-02 | 1500        |
| 101      | 2026-03-03 | 1200        |
| 101      | 2026-03-04 | 1800        |
| 101      | 2026-03-05 | 2000        |
| 102      | 2026-03-01 | 500         |
| 102      | 2026-03-02 | 700         |
| 102      | 2026-03-03 | 600         |
| 102      | 2026-03-04 | 900         |
-- Calculate the 3-day moving average of total_sales for each store_id.


SELECT
    store_id,
    trans_date,
    total_sales,
    ROUND(
        AVG(total_sales) OVER (
            PARTITION BY store_id
            ORDER BY trans_date
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2
    ) AS moving_avg_3_days
FROM transaction_summary
ORDER BY store_id, trans_date;