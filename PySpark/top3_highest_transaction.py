'''You are working on a large banking dataset (500+ GB). The dataset contains customer transactions.

Schema: transaction_id (string) customer_id (string) transaction_type (string) -- credit/debit amount (double) transaction_timestamp (timestamp)

Business Requirement: 1. Find the top 3 highest transactions per customer. 2. The dataset is huge, so performance optimization is important. 
3. The solution should scale efficiently in a distributed environment.'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

# 1. Create Spark Session
spark = SparkSession.builder.appName("Top3_Transactions_Per_Customer").getOrCreate()

# -------------------------------
# 2. Create Sample Transactions Data (simulate large dataset)
# -------------------------------
data = [("T001", "C001", "credit", 500.0, "2024-03-01 10:00:00"), ("T002", "C001", "debit", 1200.0, "2024-03-01 12:00:00"), ("T003", "C001", "credit", 700.0, "2024-03-02 09:00:00"),
    ("T004", "C001", "debit", 1500.0, "2024-03-03 11:00:00"), ("T005", "C002", "credit", 2000.0, "2024-03-01 10:30:00"), ("T006", "C002", "debit", 800.0, "2024-03-02 14:00:00"),
    ("T007", "C002", "credit", 2500.0, "2024-03-03 16:00:00"), ("T008", "C002", "debit", 300.0, "2024-03-04 18:00:00"), ("T009", "C003", "credit", 400.0, "2024-03-01 09:00:00"),
    ("T010", "C003", "debit", 900.0, "2024-03-02 10:00:00"), ("T011", "C003", "credit", 1100.0, "2024-03-03 12:00:00"), ("T012", "C003", "debit", 600.0, "2024-03-04 13:00:00")]

df = spark.createDataFrame(data, ["transaction_id", "customer_id", "transaction_type", "amount", "transaction_timestamp"])

# 3. Optimization Step 1: Repartition by customer_id # (ensures better distribution for window function)
df = df.repartition("customer_id")

# 4. Optimization Step 2: Window Function
window_spec = Window.partitionBy("customer_id").orderBy(col("amount").desc())

df_ranked = df.withColumn("rank", row_number().over(window_spec))

# 5. Filter Top 3 Transactions per Customer
top3_df = df_ranked.filter(col("rank") <= 3)

# 6. Final Output
result_df = top3_df.select("customer_id", "transaction_id", "transaction_type", "amount", "transaction_timestamp")

# 7. Show Result
result_df.show()