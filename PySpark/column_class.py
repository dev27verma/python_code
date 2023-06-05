from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Column Class").getOrCreate()

data = [("James", 23), ("Ann", 40)]
df = spark.createDataFrame(data).toDF("name.fname", "gender")
df.printSchema()

# Using DataFrame object (df)
df.select(df.gender).show()
df.select(df["gender"]).show()
# Accessing column name with dot (with backticks)
df.select(df["`name.fname`"]).show()

# Using SQL col() function
from pyspark.sql.functions import col

df.select(col("gender")).show()
# Accessing column name with dot (with backticks)
df.select(col("`name.fname`")).show()
