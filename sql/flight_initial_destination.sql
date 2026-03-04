input
| id | flight | from_city | to_city |
| -- | ------ | --------- | ------- |
| 1  | f1     | del       | hyd     |
| 1  | f2     | hyd       | blr     |
| 2  | f3     | mum       | agra    |
| 2  | f4     | agra      | kol     |

output
| id | initial | destination |
| -- | ------- | ----------- |
| 1  | del     | blr         |
| 2  | mum     | kol         |

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