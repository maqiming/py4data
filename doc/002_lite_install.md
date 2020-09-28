# 环境准备-单机模式

#### 1.1 python3安装
``` shell script
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
wget https://npm.taobao.org/mirrors/python/3.7.9/Python-3.7.9.tar.xz
tar -xvf Python-3.7.9.tar.xz -C /home/
cd /home/Python-3.7.9
./configure prefix=/usr/local/python3
make && make install
```

#### 1.2 python3配置
```shell script
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3
```

#### 2.1 jdk安装
```
wget https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jdk/x64/linux/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u265b01_openj9-0.21.0.tar.gz
tar -zxvf OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u265b01_openj9-0.21.0.tar.gz -C /usr/local/
```
#### 2.2 java配置
将解压后的文件夹重命名为jdk方便使用   
在 /etc/profile 文件添加内容   
```
export JAVA_HOME=/usr/local/jdk
export JRE_HOME=${JAVA_HOME}/jre
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/
```

#### 6 pyspark安装
```shell script
pip3 install pyspark -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

#### 7 测试
使前述各项配置立即生效
```
source /etc/profile
```
安装基础包
```shell script
pip3 install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```
测试脚本
```
import numpy as np
import pandas as pd
import os
import math
import pyspark
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import *
from time import time
from pyspark.ml.linalg import Vectors
from pyspark.sql.functions import min, max,monotonically_increasing_id
from pyspark.sql.types import *

spark=SparkSession.builder.config("spark.default.parallelism", 3000).appName("taSpark").getOrCreate()

data = spark.read.csv('data/test.csv',header=None, inferSchema="true")

data.show()


```
#### Done