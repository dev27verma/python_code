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
-- employees earning more than their manager using salary_history table
WITH latest_salary AS (
    SELECT emp_id,
           salary,
           ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY effective_date DESC) rn
    FROM salary_history
)
SELECT e.emp_name
FROM employees e
JOIN latest_salary emp
    ON e.emp_id = emp.emp_id AND emp.rn = 1
JOIN latest_salary mgr
    ON e.manager_id = mgr.emp_id AND mgr.rn = 1
WHERE emp.salary > mgr.salary;