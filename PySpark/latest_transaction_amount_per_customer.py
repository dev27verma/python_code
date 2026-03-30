'''You receive two DataFrames:
1. customer_df                                          2. transaction_df
| Column Name | Type |                                  | Column Name | Type |
| ----------- | ------ |                                | ----------------- | ---------------------------- |
| `cust_id` | string |                                  | `trans_id` | string |
| `name` | string |                                     | `cust_id` | string |
| `country` | string |                                  | `amount` | double |
                                                        | `trans_timestamp` | string (yyyy-MM-dd HH:mm:ss) |

Your manager wants the following **Customer Transaction Insights Report**:
1. Convert `trans_timestamp` to proper timestamp. 2. Determine the **latest transaction amount** for each customer. 3. Join this information with `customer_df`.
4. If a customer has **no transactions**, show `latest_amount = 0`. 5. Output columns: `cust_id`, `name`, `country`, `latest_amount` 6. Sort by `latest_amount` descending.'''
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Initialize Spark
spark = SparkSession.builder.appName("latest_transaction_amount_per_customer").getOrCreate()

customer_data = [("C1", "Alice", "India"), ("C2", "Bob", "USA"), ("C3", "Charlie", "UK"), ("C4", "David", "India")]

transaction_data = [("T1", "C1", 100.0, "2024-01-01 10:00:00"), ("T2", "C1", 200.0, "2024-02-01 12:00:00"), ("T3", "C2", 300.0, "2024-01-15 09:00:00"),
                    ("T4", "C2", 150.0, "2024-03-01 08:00:00"), ("T5", "C3", 400.0, "2024-02-10 14:00:00")]

customer_df = spark.createDataFrame(customer_data, ["cust_id", "name", "country"])

transaction_df = spark.createDataFrame(transaction_data, ["trans_id", "cust_id", "amount", "trans_timestamp"])

# Convert to timestamp
transaction_df = transaction_df.withColumn("trans_timestamp", F.to_timestamp("trans_timestamp", "yyyy-MM-dd HH:mm:ss"))

# Window to get latest transaction per customer
window_spec = Window.partitionBy("cust_id").orderBy(F.col("trans_timestamp").desc())

latest_trans_df = transaction_df.withColumn("rn", F.row_number().over(window_spec)).filter(F.col("rn") == 1).select("cust_id", F.col("amount").alias("latest_amount"))

# Join with customer data
result_df = customer_df.join(latest_trans_df, on="cust_id", how="left")

# Handle nulls for customers with no transactions
result_df = result_df.fillna({"latest_amount": 0})

# Final selection & sorting
result_df = result_df.select("cust_id", "name", "country", "latest_amount").orderBy(F.col("latest_amount").desc())

# 3. OUTPUT
result_df.show()