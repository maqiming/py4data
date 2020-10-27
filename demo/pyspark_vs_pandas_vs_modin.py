import os
import sys
import datetime
import numpy as np

import pyspark
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import *
from pyspark.ml.linalg import Vectors
from pyspark.sql.functions import countDistinct, sum
from pyspark.sql.types import *

cache_dir='/home/'

goods_cache=cache_dir+'data_goods.csv'
stock_cache=cache_dir+'data_stock.csv'

import findspark
findspark.init()

def test_pyspark():
    start=datetime.datetime.now()

    spark=SparkSession.builder.config("spark.default.parallelism", 3000).appName("taSpark").getOrCreate()
    df_stock = spark.read.csv(stock_cache,header=True)
    df2=df_stock.groupBy(['城市','客户']).agg(
        sum("库存").alias("求和"),
        countDistinct("商品编码").alias("去重计数")
    )
    df2.show(truncate=False)
    end = datetime.datetime.now()
    print('\n\n PySpark   运行时长     '+str(end-start)+'\n\n')

def test_pandas():
    start=datetime.datetime.now()

    import pandas as pd
    df_stock=pd.read_csv(stock_cache)
    df2=df_stock.groupby(['城市','客户']).agg({'库存':np.sum,'商品编码':pd.Series.nunique}).reset_index()
    df2.rename(columns={'库存':'求和','商品编码':'去重计数'},inplace=True)
    print(df2.head())

    end = datetime.datetime.now()
    print('\n\n Pandas   运行时长     '+str(end-start)+'\n\n')

def test_modin():
    start=datetime.datetime.now()
    import modin.pandas as pd

    df_stock=pd.read_csv(stock_cache)
    df2=df_stock.groupby(['城市','客户']).agg({'库存':np.sum,'商品编码':pd.Series.nunique}).reset_index()
    df2.rename(columns={'库存':'求和','商品编码':'去重计数'},inplace=True)
    print(df2.head())
    end = datetime.datetime.now()
    print('\n\n Modin   运行时长     '+str(end-start)+'\n\n')





def test_pyspark_join():
    start=datetime.datetime.now()

    spark=SparkSession.builder.config("spark.default.parallelism", 3000).appName("taSpark").getOrCreate()
    df_good = spark.read.csv(goods_cache,header=True)
    df_stock = spark.read.csv(stock_cache,header=True)
    df=df_stock.join(df_good,['城市','商品编码'],'left')

    df2=df.groupBy(['城市','客户']).agg(
        sum("库存").alias("求和"),
        countDistinct("商品编码").alias("去重计数")
    )
    df2.show(truncate=False)
    end = datetime.datetime.now()
    print('\n\n PySpark   运行时长     '+str(end-start)+'\n\n')


def test_pandas_join():
    start=datetime.datetime.now()

    import pandas as pd
    df_stock=pd.read_csv(stock_cache)
    df_goods=pd.read_csv(goods_cache)

    df=pd.merge(df_stock,df_goods,on=['城市','商品编码'],how='left')

    df2=df.groupby(['城市','客户']).agg({'库存':np.sum,'商品编码':pd.Series.nunique}).reset_index()
    df2.rename(columns={'库存':'求和','商品编码':'去重计数'},inplace=True)
    print(df2.head())

    end = datetime.datetime.now()
    print('\n\n Pandas   运行时长     '+str(end-start)+'\n\n')

def test_modin_join():

    import os
    os.environ["MODIN_OUT_OF_CORE"]='true'
    os.environ["MODIN_MEMORY"]='200000000000'
    start=datetime.datetime.now()
    import modin.pandas as pd

    df_stock=pd.read_csv(stock_cache)
    df_goods=pd.read_csv(goods_cache)
    df=pd.merge(df_stock,df_goods,on=['城市','商品编码'],how='left')

    df2=df.groupby(['城市','客户']).agg({'库存':np.sum,'商品编码':pd.Series.nunique}).reset_index()
    df2.rename(columns={'库存':'求和','商品编码':'去重计数'},inplace=True)
    print(df2.head())
    end = datetime.datetime.now()
    print('\n\n Modin   运行时长     '+str(end-start)+'\n\n')



if __name__ == "__main__":
    # test_modin()
    # test_pandas()
    # test_pyspark()

    test_modin_join()
    # test_pandas_join()
    # test_pyspark_join()