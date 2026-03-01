id flight source destination timestamp
1  indigo  india    bhutan   2022-07-11 10:00:00
2  airasia  aus     india       2022-07-11 11:00:00
3   indigo  bhutan  nepal  2022-07-11 18:00:00
4   spice   srilanka  bhutan 2022-07-12 9:00:00
5    indigo nepal  srilanka   2022-07-12 11:00:00
6    airasia india    japan      2022-07-13 15:00:00
7    spice  bhutan  nepal     2022-07-12 20:00:00

--    output
flight   source   destination
indigo    india    srilanka
airasia   aus      japan
spice     srilanka nepal

-- write sql query: For each flight, find the starting country and the final destination country of the complete journey.

WITH all_locations AS (
  -- Count how many times a location appears as SOURCE
  SELECT
    flight,
    source AS location,
    COUNT(*) OVER (PARTITION BY flight, source) AS source_cnt, 0 AS dest_cnt
  FROM flights

  UNION ALL

  -- Count how many times a location appears as DESTINATION
  SELECT
    flight,
    destination AS location,
    0 AS source_cnt,
    COUNT(*) OVER (PARTITION BY flight, destination) AS dest_cnt
  FROM flights
),

final_counts AS (
  SELECT
    flight,
    location,
    SUM(source_cnt) AS source_cnt,
    SUM(dest_cnt) AS dest_cnt
  FROM all_locations
  GROUP BY flight, location
)

SELECT
  flight,
  MAX(CASE WHEN dest_cnt = 0 THEN location END) AS source,
  MAX(CASE WHEN source_cnt = 0 THEN location END) AS destination
FROM final_counts
GROUP BY flight
ORDER BY flight;