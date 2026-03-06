employee_salary                      cte salary_comparison  cte raise_flag     cte consecutive_check                     output
| emp_id | emp_name | year | salary | prev_salary (Step1) | is_raise (Step2) | prev_raise (Step3) |              | emp_id | emp_name | year |
| ------ | -------- | ---- | ------ | ------------------- | ---------------- | ------------------ |              | ------ | -------- | ---- |
| 1      | John     | 2021 | 50000  | NULL                | 0                | NULL               |              | 1      | John     | 2023 |
| 1      | John     | 2022 | 55000  | 50000               | 1                | 0                  |              | 4      | Emma     | 2023 |
| 1      | John     | 2023 | 60000  | 55000               | 1                | 1                  |
| 2      | Smith    | 2021 | 40000  | NULL                | 0                | NULL               |
| 2      | Smith    | 2022 | 42000  | 40000               | 1                | 0                  |
| 2      | Smith    | 2023 | 41000  | 42000               | 0                | 1                  |
| 3      | David    | 2021 | 45000  | NULL                | 0                | NULL               |
| 3      | David    | 2022 | 43000  | 45000               | 0                | 0                  |
| 3      | David    | 2023 | 47000  | 43000               | 1                | 0                  |
| 4      | Emma     | 2021 | 30000  | NULL                | 0                | NULL               |
| 4      | Emma     | 2022 | 35000  | 30000               | 1                | 0                  |
| 4      | Emma     | 2023 | 40000  | 35000               | 1                | 1                  |
--Write SQl query to get the employee who got salary hike in consecutive year
WITH salary_comparison AS (                                                        -- Gets the previous year's salary for each employee.
    SELECT emp_id, emp_name, year, salary,
        LAG(salary) OVER (PARTITION BY emp_id ORDER BY year) AS prev_salary        -- LAG(salary) → returns salary from previous row
    FROM employee_salary                                                           -- PARTITION BY emp_id → calculates separately for each employee
),
raise_flag AS (                                                                    -- Identifies whether salary increased compared to previous year.SELECT *,
     CASE
        WHEN salary > prev_salary THEN 1
        ELSE 0
     END AS is_raise
FROM salary_comparison
),
consecutive_check AS (                                                              -- Checks whether the previous year also had a raise.
    SELECT *,
           LAG(is_raise) OVER (PARTITION BY emp_id ORDER BY year) AS prev_raise
    FROM raise_flag
)
SELECT DISTINCT emp_id, emp_name
FROM consecutive_check
WHERE is_raise = 1 AND prev_raise = 1;

-- in the above table step1, step2, step3 is given for each cte