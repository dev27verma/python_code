| user_id | login_date |
| ------- | ---------- |
| 101     | 2024-01-01 |
| 101     | 2024-01-05 |
| 101     | 2024-01-10 |
| 101     | 2024-01-15 |
| 101     | 2024-01-20 |
| 101     | 2024-01-25 |
| 101     | 2024-01-30 |
| 102     | 2024-02-01 |
| 102     | 2024-02-03 |
| 102     | 2024-02-05 |
| 102     | 2024-02-07 |
| 102     | 2024-02-09 |
| 103     | 2024-03-01 |
| 103     | 2024-03-04 |
| 103     | 2024-03-08 |

-- Write an SQL query to retrieve the 1st, 3rd, 5th, and 7th most recent login dates for each user.

SELECT user_id, login_date
FROM (
    SELECT
        user_id,
        login_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY login_date DESC
        ) AS rn
    FROM employee
) t
WHERE rn IN (1,3,5,7);