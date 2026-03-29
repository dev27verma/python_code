'''You are working in a telecom company. You have two large datasets:
1️⃣ customers (200M records)
customer_id (string) name (string) city (string) signup_date (date)

2️⃣ transactions (2B records)
transaction_id (string) customer_id (string) amount (double) transaction_date (date)

Business Requirement:
1. Find total transaction amount per customer. 2. Join with customer table to get customer details. 3. The join must be optimized (transactions table is extremely large).
4. Output should contain: * customer_id * name * city * total_amount

How would you implement this in an optimized way?'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, broadcast

# 1. Create Spark Session
spark = SparkSession.builder.appName("TelecomOptimizedJoin").master("local[*]").getOrCreate()

# 2. Create Customers Data (Dimension Table)
customers_data = [("C001", "Dev", "Delhi", "2023-01-01"), ("C002", "Amit", "Mumbai", "2023-02-10"), (
    "C003", "Sara", "Bangalore", "2023-03-15"), ("C004", "John", "Chennai", "2023-04-20")]

customers_df = spark.createDataFrame(customers_data, ["customer_id", "name", "city", "signup_date"])

# 3. Create Transactions Data (Fact Table)
transactions_data = [("T001", "C001", 500.0, "2024-03-01"), ("T002", "C001", 700.0, "2024-03-02"), ("T003", "C002", 1200.0, "2024-03-01"), ("T004", "C003", 300.0, "2024-03-03"),
    ("T005", "C002", 800.0, "2024-03-04"), ("T006", "C004", 1500.0, "2024-03-02"), ("T007", "C001", 200.0, "2024-03-05")]

transactions_df = spark.createDataFrame(transactions_data, ["transaction_id", "customer_id", "amount", "transaction_date"])

# 4. Optimization Step 1: Aggregate First
txn_agg_df = transactions_df.groupBy("customer_id").agg(sum("amount").alias("total_amount"))

# 5. Optimization Step 2: Select Required Columns Only
customers_small = customers_df.select("customer_id", "name", "city")

# 6. Optimization Step 3: Broadcast Join
final_df = txn_agg_df.join(broadcast(customers_small), on="customer_id", how="inner")

# 7. Final Output
result_df = final_df.select("customer_id", "name", "city", "total_amount")

# 8. Show Result
result_df.show()