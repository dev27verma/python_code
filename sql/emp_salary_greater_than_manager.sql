| emp_name | emp_salary | manager_name |
| -------- | ---------- | ------------ |
| Dev1     | 130000     | Dev4         |
| Dev3     | 115000     | Dev2         |
| Dev2     | 90000      | Dev4         |
| Dev4     | 140000     | Dev9         |
| Dev5     | 105000     | Dev9         |
| Dev6     | 150000     | Dev4         |
| Dev7     | 95000      | Dev5         |
| Dev8     | 160000     | Dev6         |
| Dev9     | 100000     | Dev6         |

-- Write SQL to find the employee having salary more than Manager
--method 1
SELECT
    e.emp_name, e.emp_salary, e.manager_name, m.emp_salary AS manager_salary
FROM employees e
JOIN employees m
    ON e.manager_name = m.emp_name
WHERE e.emp_salary > m.emp_salary;
------------------------------------------------------
-- method 2
SELECT e.emp_name
FROM employees e
JOIN salary_history s1
  ON e.emp_id = s1.emp_id
JOIN (
    SELECT emp_id, MAX(salary) AS max_salary
    FROM salary_history
    GROUP BY emp_id
) s2
  ON e.manager_id = s2.emp_id
WHERE s1.salary > s2.max_salary;