| emp_id | emp_name | hire_date  |
| ------ | -------- | ---------- |
| 1      | A        | 2020-01-10 |
| 2      | B        | 2021-06-15 |
| 3      | C        | 2019-03-20 |
| 4      | D        | 2018-11-05 |
| 5      | E        | 2022-02-01 |

-- Write an SQL query to display employee name along with hire date in DDMMYY format as a single string.
SELECT CONCAT(emp_name, ' - ', TO_CHAR(hire_date, 'DDMMYY')) AS emp_details
FROM employee;
