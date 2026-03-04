'''input
col1  col2    col3       col4     col5
xyz   abc   2024/05/01 9999/12/31 klm

output
col1  col2       col3      col4       col5
xyz   abc     2024/05/01 2026/103/04  klm
xyz           2026/03/04 9999/12/31

write pyspark code for this'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, current_date, date_format

spark = SparkSession.builder.getOrCreate()

# Sample data
data = [("xyz", "abc", "2024/05/01", "9999/12/31", "klm")]

columns = ["col1", "col2", "col3", "col4", "col5"]

df = spark.createDataFrame(data, columns)

# Get today's date in required format
today = date_format(current_date(), "yyyy/MM/dd")

# Row 1: Update col4 with today's date
df1 = df.withColumn(
    "col4",
    when(col("col4") == "9999/12/31", today).otherwise(col("col4"))
)

# Row 2: Create new row only when col4 = 9999/12/31
df2 = df.filter(col("col4") == "9999/12/31") \
    .select(
        col("col1"),
        lit("").alias("col2"),
        today.alias("col3"),
        col("col4"),
        lit("").alias("col5")
    )

# Final Output
final_df = df1.union(df2)

final_df.show(truncate=False)