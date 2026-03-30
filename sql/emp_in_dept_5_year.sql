| emp_id | emp_name | dept_id | dept_join_date |
| ------ | -------- | ------- | -------------- |
| 1      | A        | 10      | 2015-01-10     |
| 2      | B        | 20      | 2021-06-15     |
| 3      | C        | 10      | 2018-03-20     |
| 4      | D        | 30      | 2010-11-05     |
| 5      | E        | 10      | 2022-02-01     |
| 6      | F        | 20      | 2017-07-25     |
| 7      | G        | 30      | 2019-09-12     |

-- Write an SQL query to list employees in each department who have worked in that department for more than 5 years.
SELECT emp_id, emp_name, dept_id
FROM employee
WHERE dept_join_date <= CURRENT_DATE - INTERVAL '5 years';
