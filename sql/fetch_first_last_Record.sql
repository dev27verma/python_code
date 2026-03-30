| emp_id | emp_name | salary |
| ------ | -------- | ------ |
| 1      | A        | 10000  |
| 2      | B        | 20000  |
| 3      | C        | 30000  |
| 4      | D        | 25000  |
| 5      | E        | 15000  |

-- Write an SQL query to fetch the first and last record from the employee table.
SELECT *
    FROM (
        SELECT *,
            ROW_NUMBER() OVER (ORDER BY emp_id) AS rn_asc,
            ROW_NUMBER() OVER (ORDER BY emp_id DESC) AS rn_desc
        FROM employee
        ) t
WHERE rn_asc = 1 OR rn_desc = 1;
