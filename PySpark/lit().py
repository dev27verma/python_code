# lit is used to add new columns
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.appName("Lit Function").getOrCreate()

data = [("111",50000),("222",60000),("333",40000)]
schema = StructType([
    StructField("Emp_Id", StringType(),True),
    StructField("Salary", StringType(),True)
])

df = spark.createDataFrame(data, schema)
df.show()
df1 = df.select(col("Emp_Id"), col("Salary"), lit("1").alias("lit1"))
df1.show()