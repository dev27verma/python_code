from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType,StructField
from pyspark.sql.types import StringType, IntegerType, ArrayType

# Create SparkSession object
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Create data
data = [
    (("James","","Smith"),["Java","Scala","C++"],"OH","M"),
    (("Anna","Rose",""),["Spark","Java","C++"],"NY","F"),
    (("Julia","","Williams"),["CSharp","VB"],"OH","F"),
    (("Maria","Anne","Jones"),["CSharp","VB"],"NY","M"),
    (("Jen","Mary","Brown"),["CSharp","VB"],"NY","M"),
    (("Mike","Mary","Williams"),["Python","VB"],"OH","M")
 ]

# Create schema
schema = StructType([
     StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
         StructField('lastname', StringType(), True)
     ])),
     StructField('languages', ArrayType(StringType()), True),
     StructField('state', StringType(), True),
     StructField('gender', StringType(), True)
 ])

# Create dataframe
df = spark.createDataFrame(data = data, schema = schema)
df.printSchema()
df.show(truncate=False)

# Using equal condition
df.filter(df.state == "OH").show(truncate=False)

# Not equals condition
df.filter(df.state != "OH").show(truncate=False)

# using column
df.filter(col("state") == "OH").show(truncate=False)

# Using SQL Expression
df.filter("gender == 'M'").show()

# For not equal
df.filter("gender != 'M'").show()
df.filter("gender <> 'M'").show()

# Filter multiple conditions
df.filter( (df.state  == "OH") & (df.gender  == "M") ).show(truncate=False)
df.filter( (df.state  == "OH") | (df.gender  == "M") ).show(truncate=False)

# Filter IS IN List values
li=["OH","CA","DE"]
df.filter(df.state.isin(li)).show()


# Using startswith
df.filter(df.state.startswith("N")).show()
#using endswith
df.filter(df.state.endswith("H")).show()

#contains
df.filter(df.state.contains("H")).show()

# like - SQL LIKE pattern
df.filter(df.name.middlename.like("%ose%")).show()
