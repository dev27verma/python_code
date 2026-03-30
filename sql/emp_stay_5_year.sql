| emp_id | emp_name | join_date  |
| ------ | -------- | ---------- |
| 1      | A        | 2015-01-10 |
| 2      | B        | 2021-06-15 |
| 3      | C        | 2018-03-20 |
| 4      | D        | 2010-11-05 |
| 5      | E        | 2022-02-01 |

-- Write an SQL query to find employees who have been in the company for more than 5 years.
SELECT emp_id, emp_name
FROM employee
WHERE join_date <= CURRENT_DATE - INTERVAL '5 years';
