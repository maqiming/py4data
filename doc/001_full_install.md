# 环境准备-Hadoop+Spark

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

#### 3.1 Scala安装
```
wget https://downloads.lightbend.com/scala/2.13.3/scala-2.13.3.tgz
tar -zxvf scala-2.13.3.tgz -C /usr/local/
```
#### 3.2 Scala配置
将解压后的文件夹重命名为jdk方便使用  
在 /etc/profile 文件添加内容
```
export SCALA_HOME=/usr/local/scala
export PATH=$SCALA_HOME/bin:$PATH
```

#### 4.1 Hadoop安装
```
wget https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz
tar -zxvf hadoop-2.7.7.tar.gz -C /usr/local/
```
#### 4.2 Hadoop配置
同样，将解压后的文件夹重命名为hadoop
在 /etc/profile 文件添加内容 
```
export HADOOP_HOME=usr/local/hadoop
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
```
core-site.xml
```XML
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://localhost:9000</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/var/hadoop/hadoop-\${user.name}</value>
    </property>
</configuration>
```

hdfs-site.xml
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```

mapred-site.xml
```xml
<configuration>
    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>localhost:10020</value>
    </property>
    <!-- 配置web端口 -->
    <property>
        <name>mapreduce.jobhistory.webapp.address</name>
        <value>localhost:19888</value>
    </property>
    <!-- 配置正在运行中的日志在hdfs上的存放路径 -->
    <property>
        <name>mapreduce.jobhistory.intermediate-done-dir</name>
        <value>/history/done_intermediate</value>
    </property>
    <!-- 配置运行过的日志存放在hdfs上的存放路径 -->
    <property>
        <name>mapreduce.jobhistory.done-dir</name>
        <value>/history/done</value>
    </property>
</configuration>
```

yarn-site.xml
```xml
<configuration>
    <property>
        <name>yarn.log-aggregation-enable</name>
        <value>true</value>
    </property>
</configuration>
```

#### 4.3 Hadoop启动停止
```shell script
/usr/local/hadoop/sbin/start-all.sh
/usr/local/hadoop/sbin/stop-all.sh
```

#### 5.1 Spark安装
```
wget https://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
tar -zxvf spark-2.4.7-bin-hadoop2.7.tgz -C /usr/local/
```
#### 5.2 Spark配置
同样，将解压后的文件夹重命名为spark方便使用
```
export SPARK_HOME=/usr/local/spark
export PATH=$SPARK_HOME/bin:$PATH
export PYSPARK_PYTHON=python3
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
pip3 install findspark -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```
测试脚本
```Python
import findspark
findspark.init() # 用于获取spark

import pandas as pd
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('my_first_app').getOrCreate()
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=['row1', 'row2'],
                   columns=['c1', 'c2', 'c3'])
spark_df=spark.createDataFrame(df)
spark_df.show()
print('successful')
```
#### Done