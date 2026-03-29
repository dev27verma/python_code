'''You are working in an ad-tech company. You receive clickstream data daily.
Schema: user_id (string) session_id (string) event_type (string) -- click/view/purchase event_time (timestamp) page_url (string)

Business Requirement: 1. Identify user sessions.
2. A session is defined as: * Events of same `user_id` * Gap between consecutive events ≤ 30 minutes * If gap > 30 minutes → new session
3. Assign a unique session number per user. 4. Dataset size: 800M+ records.  5. Solution must be scalable and optimized.'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lag, when, sum
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("user_session").getOrCreate()

data = [("U1","S1","click","2024-03-01 10:00:00","/home"), ("U1","S1","view","2024-03-01 10:10:00","/prod"),
("U1","S1","click","2024-03-01 11:00:00","/cart"), ("U1","S1","purchase","2024-03-01 11:20:00","/pay"),
("U2","S2","click","2024-03-01 09:00:00","/home"), ("U2","S2","view","2024-03-01 10:00:00","/prod")]

df = spark.createDataFrame(data, ["user_id","session_id","event_type","event_time","page_url"])

w = Window.partitionBy("user_id").orderBy("event_time")

df_session = (df.withColumn("prev_time", lag("event_time").over(w)).withColumn("time_diff", (col("event_time").cast("long") - col("prev_time").cast("long"))/60)
              .withColumn("new_session_flag", when(col("time_diff").isNull() | (col("time_diff") > 30), 1)
                          .otherwise(0)).withColumn("session_number", sum("new_session_flag").over(w)))

df_session.select("user_id","event_time","session_number").show()