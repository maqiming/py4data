import time

import datetime


import findspark
findspark.init()


import os
import sys

par_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(par_dir)

sys.path.append("/home/maqiming/qyt_report")

from koala import prdk
import numpy as np

import pyspark
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import *
from pyspark.ml.linalg import Vectors
from pyspark.sql.functions import countDistinct, sum
from pyspark.sql.types import *

cache_dir='/home/maqiming/qyting/qyt_cache_dir/cache_dyy_cres/'

goods_cache=cache_dir+'cres_customer_goods_20200929.csv'
stock_cache=cache_dir+'cres_org_store_20200929.csv'



def test_pyspark():
    start=datetime.datetime.now()

    spark=SparkSession.builder.config("spark.default.parallelism", 3000).appName("taSpark").getOrCreate()
    df_stock = spark.read.csv(stock_cache,header=True)
    df2=df_stock.groupBy(['customer_id','erporg_id']).agg(
        sum("stock_num").alias("求和"),
        countDistinct("erp_goods_code").alias("去重计数")
    )
    df2.show(truncate=False)
    end = datetime.datetime.now()
    print('\n\n PySpark   运行时长     '+str(end-start)+'\n\n')

def test_pandas():
    start=datetime.datetime.now()

    import pandas as pd
    df_stock=pd.read_csv(stock_cache)
    df2=df_stock.groupby(['customer_id','erporg_id']).agg({'stock_num':np.sum,'erp_goods_code':pd.Series.nunique}).reset_index()
    df2.rename(columns={'stock_num':'求和','erp_goods_code':'去重计数'},inplace=True)
    print(df2.head())

    end = datetime.datetime.now()
    print('\n\n Pandas   运行时长     '+str(end-start)+'\n\n')

def test_modin():
    start=datetime.datetime.now()
    import modin.pandas as pd

    df_stock=pd.read_csv(stock_cache)
    df2=df_stock.groupby(['customer_id','erporg_id']).agg({'stock_num':np.sum,'erp_goods_code':pd.Series.nunique}).reset_index()
    df2.rename(columns={'stock_num':'求和','erp_goods_code':'去重计数'},inplace=True)
    print(df2.head())
    end = datetime.datetime.now()
    print('\n\n Modin   运行时长     '+str(end-start)+'\n\n')





def test_pyspark_join():
    start=datetime.datetime.now()

    spark=SparkSession.builder.config("spark.default.parallelism", 3000).appName("taSpark").getOrCreate()
    df_good = spark.read.csv(goods_cache,header=True)
    df_stock = spark.read.csv(stock_cache,header=True)
    df=df_stock.join(df_good,['customer_id','erp_goods_code'],'left')

    df2=df.groupBy(['customer_id','erporg_id']).agg(
        sum("stock_num").alias("求和"),
        countDistinct("standard_code").alias("去重计数")
    )
    df2.show(truncate=False)
    end = datetime.datetime.now()
    print('\n\n PySpark   运行时长     '+str(end-start)+'\n\n')


def test_pandas_join():
    start=datetime.datetime.now()

    import pandas as pd
    df_stock=pd.read_csv(stock_cache)
    df_goods=pd.read_csv(goods_cache)

    df=pd.merge(df_stock,df_goods,on=['customer_id','erp_goods_code'],how='left')

    df2=df.groupby(['customer_id','erporg_id']).agg({'stock_num':np.sum,'standard_code':pd.Series.nunique}).reset_index()
    df2.rename(columns={'stock_num':'求和','standard_code':'去重计数'},inplace=True)
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
    df=pd.merge(df_stock,df_goods,on=['customer_id','erp_goods_code'],how='left')

    df2=df.groupby(['customer_id','erporg_id']).agg({'stock_num':np.sum,'standard_code':pd.Series.nunique}).reset_index()
    df2.rename(columns={'stock_num':'求和','standard_code':'去重计数'},inplace=True)
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