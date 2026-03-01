-- update employee email from yahoo.com to gmail.com
UPDATE your_table_name SET your_column_name = REPLACE(your_column_name, '@gmail.com', '@ymail.com') WHERE your_column_name LIKE '%@gmail.com';
-------------------------------------------------
-- sql queries to get five char of employee name:
SELECT SUBSTRING(employee_name, 1, 5) AS first_five_characters
FROM your_table_name;

SELECT LEFT(employee_name, 5) AS first_five_characters
FROM your_table_name;
----------------------------------------------------
--    c1 c2                output
--    1   a                c1   c2
--    1   b                1    a,b
--    2   c                2    c

SELECT c1, STRING_AGG(c2, ',') AS c2 FROM your_table GROUP BY c1;
------------------------------------------------------------
-- sql query to fetch 'ACL' from ORACLE
SELECT SUBSTRING('verdevkd', CHARINDEX('dev', 'verdevkd'), 3) AS result;

-----------------------------------------------------------------------------------
-- Remove null from table

DELETE FROM your_table
WHERE column IS NULL;
----------------------------------------------------------
-- find table which are modified on specific date
SELECT
  table_name
FROM
  `project_id.dataset_id.INFORMATION_SCHEMA.TABLES`
WHERE
  DATE(creation_time) = '2021-07-05'
--------------------------------------------------------
-- federated query
SELECT *
FROM EXTERNAL_QUERY(
  'your-cloud-sql-connection-name',
  'SELECT * FROM your_cloud_sql_table'
);
----------------------------------------------------------------
-- time-travel
-- BQ provides a powerful feature called "Time-Travel" or "Time-Travel Queries" that allows you to query historical data as it appeared at specific points in time.
-- This feature is especially useful for analyzing and auditing changes to your data over time.
-- Snapshot Timestamp: When querying a table in BigQuery, you can specify a snapshot timestamp to view the data as it existed at that particular point in time.
-- Query History: You can also use the __TABLES__ metadata table to query the schema of a table at different points in time to see how it has evolved.

SELECT * FROM table FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP()), INTERVAL 1 DAY);   ---> max 7 day