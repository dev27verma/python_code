# Create Empty Data Frame
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.appName("Empty Dataframe").getOrCreate()

df = spark.createDataFrame([], StructType([]))
df.printSchema()
df.show()


# Create Dataframe from Data and Schema
data = [("Finance",10,"BT"),("Marketing",20,"BT"),("Sales",30,"BT"),("IT",40,"BT")]
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age",StringType(), True),
    StructField("Org", StringType(), True)
])
df = spark.createDataFrame(data, schema)
df.show()