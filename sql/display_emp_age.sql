| emp_id | emp_name | age |
| ------ | -------- | --- |
| 1      | A        | 22  |
| 2      | B        | 27  |
| 3      | C        | 35  |
| 4      | D        | 42  |
| 5      | E        | 29  |
| 6      | F        | 31  |
| 7      | G        | 24  |
| 8      | H        | 45  |

-- Write an SQL query to display employees grouped by age bracket.
SELECT
    CASE
        WHEN age < 25 THEN 'Below 25'
        WHEN age BETWEEN 25 AND 34 THEN '25-34'
        WHEN age BETWEEN 35 AND 44 THEN '35-44'
        ELSE '45+'
    END AS age_bracket, COUNT(*) AS emp_count
FROM employee
GROUP BY age_bracket
