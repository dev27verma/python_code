                      user_activity                                                 output
| user_id  | date       | page_visited |                 | date             | home_ct | payment_ct | management_ct |
| ---------| ---------- | ------------ |                 | ---------------- | ------- | ---------- | ------------- |
| 1        | 2024-01-01 | home         |                 | 2024-01-01       | 3       | 0          | 0             |
| 1        | 2024-01-02 | payment      |                 | 2024-01-02       | 0       | 1          | 0             |
| 1        | 2024-01-03 | management   |                 | 2024-01-03       | 0       | 0          | 1             |
| 2        | 2024-01-01 | home         |
| 1        | 2024-01-01 | home         |


-- Write an SQL query to generate a daily summary report that shows:
-- Total number of visits to the home page
-- Total number of visits to the payment page
-- Total number of visits to the management page
-- The output should be in the following format:


SELECT
    date,
    SUM(CASE WHEN page_visited = 'home' THEN 1 ELSE 0 END) AS home_ct,
    SUM(CASE WHEN page_visited = 'payment' THEN 1 ELSE 0 END) AS payment_ct,
    SUM(CASE WHEN page_visited = 'management' THEN 1 ELSE 0 END) AS management_ct
FROM user_activity
GROUP BY date;
----------------------------------------------------------
-- using pivot

SELECT *
FROM (
    SELECT date, page_visited
    FROM user_activity
) t
PIVOT (
    COUNT(page_visited)
    FOR page_visited IN ('home' AS home_ct,
                         'payment' AS payment_ct,
                         'management' AS management_ct)
);