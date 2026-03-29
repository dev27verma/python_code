'''You are working in an insurance company.
You have two large datasets:
1️⃣ claims (800M records) schema: claim_id (string) customer_id (string) claim_amount (double) claim_date (date) policy_id (string)
2️⃣ policies (5M records) policy_id (string) policy_type (string) premium_amount (double) start_date (date) end_date (date)

Business Requirement: 1. Join claims with policies.
2. Keep only valid claims where: * `claim_date` is between `start_date` and `end_date` 3. Find total claim amount per policy_type.
4. Optimize the join because claims table is extremely large. 5. Ensure solution is scalable and production-ready.'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, broadcast

spark = SparkSession.builder.appName("InsuranceClaimsAnalysis").getOrCreate()

claims_data = [("C1","U1",5000.0,"2024-03-01","P1"), ("C2","U2",3000.0,"2024-03-05","P2"), ("C3","U1",7000.0,"2024-04-01","P1"), ("C4","U3",2000.0,"2024-05-01","P3")]

policies_data = [("P1","Health",1000.0,"2024-01-01","2024-12-31"), ("P2","Auto",1500.0,"2024-02-01","2024-06-30"), ("P3","Life",2000.0,"2024-01-01","2024-03-31")]

claims_df = spark.createDataFrame(claims_data, ["claim_id","customer_id","claim_amount","claim_date","policy_id"])
policies_df = spark.createDataFrame(policies_data, ["policy_id","policy_type","premium_amount","start_date","end_date"])

# Optimized join using broadcast (policies is small ~5M)
joined_df = claims_df.join(broadcast(policies_df), "policy_id")

# Filter valid claims
valid_df = joined_df.filter((col("claim_date") >= col("start_date")) & (col("claim_date") <= col("end_date")))

# Aggregate
result_df = valid_df.groupBy("policy_type").agg(_sum("claim_amount").alias("total_claim_amount"))

result_df.show()