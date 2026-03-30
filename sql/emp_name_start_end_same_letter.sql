| emp_id | emp_name |
| ------ | -------- |
| 1      | Anna     |
| 2      | Bob      |
| 3      | Charlie  |
| 4      | David    |
| 5      | Eve      |
| 6      | Ada      |
| 7      | Level    |
| 8      | Mark     |

-- Write an SQL query to find employees whose name starts and ends with the same letter.
SELECT emp_id, emp_name
FROM employee
WHERE LOWER(SUBSTRING(emp_name, 1, 1)) = LOWER(SUBSTRING(emp_name, LENGTH(emp_name), 1));

-- method 2
SELECT emp_id, emp_name
FROM employee WHERE LOWER(LEFT(emp_name, 1)) = LOWER(RIGHT(emp_name, 1
