employee_salary
| emp_id | emp_name | year | salary |
| ------ | -------- | ---- | ------ |
| 1      | John     | 2021 | 50000  |
| 1      | John     | 2022 | 55000  |
| 1      | John     | 2023 | 60000  |
| 2      | Smith    | 2021 | 40000  |
| 2      | Smith    | 2022 | 42000  |
| 2      | Smith    | 2023 | 41000  |
| 3      | David    | 2021 | 45000  |
| 3      | David    | 2022 | 43000  |
| 3      | David    | 2023 | 47000  |
| 4      | Emma     | 2022 | 30000  |
| 4      | Emma     | 2023 | 35000  |
--Write SQl query to get the employee who got salary hike in consecutive year
WITH salary_comparison AS (
    SELECT emp_id,
           emp_name,
           year,
           salary,
           LAG(salary) OVER (PARTITION BY emp_id ORDER BY year) AS prev_salary
    FROM employee_salary
),

raise_flag AS (
    SELECT *,
           CASE
               WHEN salary > prev_salary THEN 1
               ELSE 0
           END AS is_raise
    FROM salary_comparison
),

consecutive_check AS (
    SELECT *,
           LAG(is_raise) OVER (PARTITION BY emp_id ORDER BY year) AS prev_raise
    FROM raise_flag
)

SELECT DISTINCT emp_id, emp_name
FROM consecutive_check
WHERE is_raise = 1 AND prev_raise = 1;