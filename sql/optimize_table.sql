staging_orders -- new data comes daily
requirements -
    - handle updates (can be same order_id)
    - handle late data (last 2 days)
    - avoid full table scan orders
    --- large table
    -- column_name: order_id str user_id str order_date date (partition key) amount float updated_at timestamp write sql query

WITH staging_dedup AS (
    -- deduplicate and keep latest record per order_id (last 2 days only)
    SELECT order_id, user_id, order_date, amount, updated_at
    FROM (
        SELECT *,
               ROW_NUMBER() OVER (
                   PARTITION BY order_id
                   ORDER BY updated_at DESC
               ) AS rn
        FROM staging_orders
        WHERE order_date >= CURRENT_DATE - INTERVAL 2 DAY
    ) s
    WHERE rn = 1
)

MERGE INTO orders tgt
USING staging_dedup src
ON tgt.order_id = src.order_id
   AND tgt.order_date >= CURRENT_DATE - INTERVAL 2 DAY   -- partition pruning

WHEN MATCHED AND src.updated_at > tgt.updated_at THEN
  UPDATE SET
    tgt.user_id = src.user_id,
    tgt.order_date = src.order_date,
    tgt.amount = src.amount,
    tgt.updated_at = src.updated_at

WHEN NOT MATCHED THEN
  INSERT (order_id, user_id, order_date, amount, updated_at)
  VALUES (src.order_id, src.user_id, src.order_date, src.amount, src.updated_at);