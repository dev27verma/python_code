                  Input Table (flights)                                               Output Table
| id    | flight  | source   | destination | timestamp           |         | flight          | source   | destination |
| ------| ------- | -------- | ----------- | ------------------- |         |---------------- | -------- | ----------- |
| 1     | indigo  | india    | bhutan      | 2022-07-11 10:00:00 |         | indigo          | india    | srilanka    |
| 2     | airasia | aus      | india       | 2022-07-11 11:00:00 |         | airasia         | aus      | japan       |
| 3     | indigo  | bhutan   | nepal       | 2022-07-11 18:00:00 |         | spice           | srilanka | nepal       |
| 4     | spice   | srilanka | bhutan      | 2022-07-12 09:00:00 |
| 5     | indigo  | nepal    | srilanka    | 2022-07-12 11:00:00 |
| 6     | airasia | india    | japan       | 2022-07-13 15:00:00 |
| 7     | spice   | bhutan   | nepal       | 2022-07-12 20:00:00 |

-- write sql query: For each flight, find the starting country and the final destination country of the complete journey.
WITH initial_source AS (
    SELECT a.flight, a.source
    FROM flights a
    LEFT JOIN flights b
        ON a.flight = b.flight
        AND a.source = b.destination
    WHERE b.destination IS NULL
),
final_destination AS (
    SELECT a.flight, a.destination
    FROM flights a
    LEFT JOIN flights b
        ON a.flight = b.flight
        AND a.destination = b.source
    WHERE b.source IS NULL
)
SELECT i.flight,
       i.source,
       f.destination
FROM initial_source i
JOIN final_destination f
ON i.flight = f.flight;