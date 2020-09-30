import datetime

import findspark

findspark.init()

import numpy as np
import pandas as pd
import pyspark
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import *
from pyspark.ml.linalg import Vectors
from pyspark.sql.functions import countDistinct, sum
from pyspark.sql.types import *

spark = SparkSession.builder.config("spark.default.parallelism", 3000).appName("taSpark").getOrCreate()

goods_cache = 'cres_customer_goods.csv'
stock_cache = 'cres_org_store.csv'

# =====================================
# pyspark
# =====================================
start = datetime.datetime.now()
df_good = spark.read.csv(goods_cache, header=True)
df_stock = spark.read.csv(stock_cache, header=True)
df = df_stock.join(df_good, ['customer_id', 'erp_goods_code'], 'left')

df2 = df.groupBy(['customer_id', 'erporg_id']).agg(
    sum("stock_num").alias("求和"),
    countDistinct("standard_code").alias("去重计数")
)
df2.show(truncate=False)
end = datetime.datetime.now()
print('\n\n PySpark   运行时长     ' + str(end - start) + '\n\n')

# =====================================
# pandas
# =====================================
start = datetime.datetime.now()
df_stock = pd.read_csv(stock_cache)
df_goods = pd.read_csv(goods_cache)

df = pd.merge(df_stock, df_goods, on=['customer_id', 'erp_goods_code'], how='left')

df2 = df.groupby(['customer_id', 'erporg_id']).agg(
    {'stock_num': np.sum, 'standard_code': pd.Series.nunique}).reset_index()
df2.rename(columns={'stock_num': '求和', 'standard_code': '去重计数'}, inplace=True)
print(df2.head())
end = datetime.datetime.now()
print('\n\n Pandas   运行时长     ' + str(end - start) + '\n\n')
