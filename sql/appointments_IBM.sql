appointments
| email                                         | appointment_date |
| --------------------------------------------- | ---------------- |
| [dev@gmail.com](mailto:dev@gmail.com)         | 2026-02-28       |
| [anita@yahoo.com](mailto:anita@yahoo.com)     | 2026-03-01       |
| [rahul@outlook.com](mailto:rahul@outlook.com) | 2026-03-02       |
| [sneha@gmail.com](mailto:sneha@gmail.com)     | 2026-03-07       |
| [karan@gmail.com](mailto:karan@gmail.com)     | 2026-03-03       |
| [pooja@yahoo.com](mailto:pooja@yahoo.com)     | 2026-03-08       |
| [amit@company.com](mailto:amit@company.com)   | 2026-03-04       |

-- Write a SQL query to list all appointments scheduled on weekends (Saturday or Sunday).

SELECT
  email,
  FORMAT_DATE('%A', DATE(appointment_date)) AS scheduled_appointment
FROM appointments
WHERE EXTRACT(DAYOFWEEK FROM DATE(appointment_date)) IN (1, 7)
ORDER BY email ASC;
