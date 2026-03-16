"""    column_A          column_B                   output
        1         120*234*452*106*865*120           column_A   column_B   column_C
        2         230*340*230*675*230                   1           120         2
                                                        1           234         1
                                                        1           452         1
                                                        1           106         1
                                                        1           865         1
                                                        2           230         3
                                                        2           340         1
                                                        2           675         1
write pyspark code to get the above output from given columns, columnC is the occurrence of number in above column
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col, count

# Create Spark session
spark = SparkSession.builder.appName("SplitAndCount").getOrCreate()

# Sample Data
data = [
    (1, "120*234*452*106*865*120"),
    (2, "230*340*230*675*230")
]

schema = ["column_A", "column_B"]

df = spark.createDataFrame(data, schema)

# Step 1: Split column_B by *
df_split = df.withColumn("column_C", split(col("column_B"), "\\*"))

# Step 2: Explode array into rows
df_exploded = df_split.withColumn("column_B", explode(col("column_C")))

# Step 3: Group and count occurrences
result_df = df_exploded.groupBy("column_A", "column_B").agg(count("*").alias("column_C")).orderBy("column_A", "column_B")

result_df.show()