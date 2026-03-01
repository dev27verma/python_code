--    | emp_name | emp_salary | manager_name | manager_salary |
--    | -------- | ---------- | ------------ | -------------- |
--    | Dev1     | 130000     | Manager1     | 120000         |
--    | Dev3     | 115000     | Manager2     | 110000         |
--    | Dev2     | 90000      | Manager1     | 120000         |
--    | Dev4     | 140000     | Manager3     | 135000         |
--    | Dev5     | 105000     | Manager2     | 110000         |
--    | Dev6     | 150000     | Manager4     | 145000         |
--    | Dev7     | 95000      | Manager3     | 135000         |
--    | Dev8     | 160000     | Manager5     | 155000         |
--    | Dev9     | 100000     | Manager4     | 145000         |

-- Write SQL to find the employee having salary more than Manager
--method 1
SELECT e.emp_id,
       e.emp_name, e.salary   AS emp_salary, m.emp_name AS manager_name, m.salary   AS manager_salary
FROM employees e
JOIN employees m
  ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;
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