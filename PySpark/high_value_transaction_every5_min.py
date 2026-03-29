'''You are working for a fintech company. You receive streaming transaction data from Kafka in real-time.

Schema of incoming JSON data: transaction_id (string) customer_id (string) amount (double) transaction_time (timestamp)

Business Requirement: 1. Read streaming data from Kafka. 2. Parse JSON data. 3. Filter transactions where `amount > 10,000` (high-value transactions).
4. Calculate total high-value transaction amount every 5 minutes. 5. Handle late data up to 10 minutes. 6. Write the aggregated result to a Parquet sink.'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, window, sum
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType, StructField

# 1. Spark Session
spark = SparkSession.builder.appName("calculate_transaction_amount_every_5_min").getOrCreate()

# 2. Define Schema
schema = StructType([StructField("transaction_id", StringType()), StructField("customer_id", StringType()), StructField("amount", DoubleType()),
    StructField("transaction_time", TimestampType())])

# 3. Read from Kafka
df_kafka = spark.readStream.format("kafka").option("kafka.bootstrap.servers","localhost:9092").option("subscribe","transactions").load()

# 4. Parse JSON
df_parsed = df_kafka.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# 5. Filter high-value transactions
df_filtered = df_parsed.filter(col("amount") > 10000)

# 6. Window aggregation (5 min window + 10 min watermark)
df_agg = (df_filtered.withWatermark("transaction_time","10 minutes").groupBy(window(col("transaction_time"),"5 minutes"))
          .agg(sum("amount").alias("total_amount")))

# 7. Write to Parquet
query = (df_agg.writeStream.format("parquet").option("path","output/stream_parquet").option("checkpointLocation","output/checkpoint").
         outputMode("append").start())

query.awaitTermination()