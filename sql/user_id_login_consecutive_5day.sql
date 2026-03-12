table: user_activity               cte: lag_date        detect_break       create_group_id      output
| user_id | time_stamp |                prev_date        | new_group |      grp |             | user_id | start_date | end_date   | consecutive_days |
| ------- | ---------- |                ----------       | --------- |      --- |             | ------- | ---------- | ---------- | ---------------- |
| 101     | 2026-01-01 |                NULL             | 1         |      1   |             | 101     | 2026-01-01 | 2026-01-05 | 5                |
| 101     | 2026-01-02 |                2026-01-01       | 0         |      1   |
| 101     | 2026-01-03 |                2026-01-02       | 0         |      1   |
| 101     | 2026-01-04 |                2026-01-03       | 0         |      1   |
| 101     | 2026-01-05 |                2026-01-04       | 0         |      1   |
| 101     | 2026-01-07 |                2026-01-05       | 1         |      2   |
| 102     | 2026-01-01 |                NULL             | 1         |      1   |
| 102     | 2026-01-03 |                2026-01-01       | 1         |      2   |
| 102     | 2026-01-04 |                2026-01-03       | 0         |      2   |
| 102     | 2026-01-05 |                2026-01-04       | 0         |      2   |
| 102     | 2026-01-06 |                2026-01-05       | 0         |      2   |
-- user_id, time_stamp write sql query to get 5 consecutive day
WITH lag_date AS (
    SELECT
        user_id, time_stamp,
        LAG(time_stamp) OVER(PARTITION BY user_id ORDER BY time_stamp) AS prev_date
    FROM user_activity
),
detect_break AS (
    SELECT *,
        CASE
            WHEN DATE_DIFF(time_stamp, prev_date, DAY) = 1 THEN 0
            ELSE 1
        END AS new_group
    FROM lag_date
),
create_group_id AS (
    SELECT *,
        SUM(new_group) OVER(PARTITION BY user_id ORDER BY time_stamp) AS grp
    FROM detect_break
)
SELECT
    user_id, MIN(time_stamp) start_date, MAX(time_stamp) end_date, COUNT(*) consecutive_days
FROM create_group_id
GROUP BY user_id, grp
HAVING COUNT(*) >= 5;