SELECT
  email,
  FORMAT_DATE('%A', DATE(appointment_date)) AS scheduled_appointment
FROM appointments
WHERE EXTRACT(DAYOFWEEK FROM DATE(appointment_date)) IN (1, 7)
ORDER BY email ASC;
