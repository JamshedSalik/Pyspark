import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

# 1. Create Spark session
spark = SparkSession.builder \
    .appName("PlayersMatchesExample") \
    .getOrCreate()

# 2. Players table data
players_data = [
    (15, 1),
    (25, 1),
    (30, 1),
    (45, 1),
    (10, 2),
    (35, 2),
    (50, 2),
    (20, 3),
    (40, 3),
]

players_schema = StructType([
    StructField("player_id", IntegerType(), False),
    StructField("group_id", IntegerType(), False),
])

players_df = spark.createDataFrame(players_data, players_schema)

# 3. Matches table data
matches_data = [
    (1, 15, 45, 3, 0),
    (2, 30, 25, 1, 2),
    (3, 30, 15, 2, 0),
    (4, 40, 20, 5, 2),
    (5, 35, 50, 1, 1),
]

matches_schema = StructType([
    StructField("match_id", IntegerType(), False),
    StructField("first_player", IntegerType(), False),
    StructField("second_player", IntegerType(), False),
    StructField("first_score", IntegerType(), False),
    StructField("second_score", IntegerType(), False),
])

matches_df = spark.createDataFrame(matches_data, matches_schema)

# 4. (Optional) show the data
print("Players:")
players_df.show()

print("Matches:")
matches_df.show()