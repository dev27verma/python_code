input                                       output                              initial_city output                             final_city output
| id | flight | from_city | to_city |   | id | initial| destination|  |a.id|a.from_city|a.to_city| b.to_city| Match   | | a.id | a.from_city|a.to_city| b.from_city | Match   |
| -- | ------ | --------- | ------- |   | -- | -------| -----------|  |----|---------- |---------| ---------| ------- | | ---- | -----------|---------| ----------- | ------- |
| 1  | f1     | del       | hyd     |   | 1  | del    | blr        |  |1   |del        |hyd      | NULL     | ✅ Start| | 1    | del        |hyd      | hyd         | ❌      |
| 1  | f2     | hyd       | blr     |   | 2  | mum    | kol        |  |1   |hyd        |blr      | hyd      | ❌      | | 1    | hyd        |blr      | NULL        | ✅ Final|
| 2  | f3     | mum       | agra    |                                 |2   |mum        |agra     | NULL     | ✅ Start| | 2    | mum        |agra     | agra        | ❌      |
| 2  | f4     | agra      | kol     |                                 |2   |agra       |kol      | agra     | ❌      | | 2    | agra       |kol      | NULL        | ✅ Final|

WITH initial_city AS (
    SELECT a.id, a.from_city AS initial
    FROM flights a
    LEFT JOIN flights b
        ON a.id = b.id
        AND a.from_city = b.to_city
    WHERE b.to_city IS NULL
),
final_city AS (
    SELECT a.id, a.to_city AS destination
    FROM flights a
    LEFT JOIN flights b
        ON a.id = b.id
        AND a.to_city = b.from_city
    WHERE b.from_city IS NULL
)
SELECT i.id,
       i.initial,
       f.destination
FROM initial_city i
JOIN final_city f
    ON i.id = f.id;

-- initial_city: Does this from_city appear as a destination somewhere else?
| id | initial |
| -- | ------- |
| 1  | del     |
| 2  | mum     |

-- final_city: Does this destination appear as a starting city somewhere else?
| id | destination |
| -- | ----------- |
| 1  | blr         |
| 2  | kol         |

-- final_output:
-- We check if a.to_city exists as any from_city.
-- If it does not exist, that city is the final destination.
| id | initial | destination |
| -- | ------- | ----------- |
| 1  | del     | blr         |
| 2  | mum     | kol         |
