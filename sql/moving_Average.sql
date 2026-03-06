           Input Table (transaction_summary)                            Output Table
| store_id        | trans_date | total_sales |   | store_id         | trans_date | total_sales | moving_avg_3day |
| --------------- | ---------- | ----------- | - | ---------------- | ---------- | ----------- | --------------- |
| 101             | 2026-03-01 | 1000        |   | 101              | 2026-03-01 | 1000        | 1000.00         |
| 101             | 2026-03-02 | 1500        |   | 101              | 2026-03-02 | 1500        | 1250.00         |
| 101             | 2026-03-03 | 1200        |   | 101              | 2026-03-03 | 1200        | 1233.33         |
| 101             | 2026-03-04 | 1800        |   | 101              | 2026-03-04 | 1800        | 1500.00         |
| 101             | 2026-03-05 | 2000        |   | 101              | 2026-03-05 | 2000        | 1666.67         |
| 102             | 2026-03-01 | 500         |   | 102              | 2026-03-01 | 500         | 500.00          |
| 102             | 2026-03-02 | 700         |   | 102              | 2026-03-02 | 700         | 600.00          |
| 102             | 2026-03-03 | 600         |   | 102              | 2026-03-03 | 600         | 600.00          |
| 102             | 2026-03-04 | 900         |   | 102              | 2026-03-04 | 900         | 733.33          |


-- Calculate the 3-day moving average of total_sales for each store_id.
SELECT
    store_id, trans_date, total_sales,
    AVG(total_sales) OVER (PARTITION BY store_id ORDER BY trans_date ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_3_days
FROM transaction_summary
ORDER BY store_id, trans_date;



For store_id: 101
| Date   | Calculation              | Moving Avg |
| ------ | ------------------------ | ---------- |
| 01 Mar | 1000                     | 1000       |
| 02 Mar | (1000 + 1500) / 2        | 1250       |
| 03 Mar | (1000 + 1500 + 1200) / 3 | 1233.33    |
| 04 Mar | (1500 + 1200 + 1800) / 3 | 1500       |
| 05 Mar | (1200 + 1800 + 2000) / 3 | 1666.67    |
