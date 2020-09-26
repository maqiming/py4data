# 环境准备

#### 1. 安装python3
``` 
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
wget https://npm.taobao.org/mirrors/python/3.7.9/Python-3.7.9.tar.xz
tar -xvf Python-3.7.9.tar.xz -C /home/
cd Python-3.7.9
./configure prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3
```

#### 2.1 jdk安装
```
wget https://mirrors.tuna.tsinghua.edu.cn/AdoptOpenJDK/8/jdk/x64/linux/OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u265b01_openj9-0.21.0.tar.gz
tar -zxvf OpenJDK8U-jdk_x64_linux_openj9_linuxXL_8u265b01_openj9-0.21.0.tar.gz -C /usr/lib/
```
#### 2.2 java配置
将解压后的文件夹重命名为jdk方便使用   
在 /etc/profile 文件添加内容   
```
export JAVA_HOME=/usr/lib/jdk
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/
```

使文件立即生效
```
source /etc/profile
```


#### 3 Scala安装

```
wget https://downloads.lightbend.com/scala/2.13.3/scala-2.13.3.tgz

```

修改

```
SCALA_HOME=/usr/lib/scala
PATH=$SCALA_HOME/bin:$PATH
```


#### 3.1 Hadoop安装
```
wget https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz
tar -zxvf hadoop-2.7.7.tar.gz -C /usr/lib/
```
#### 3.2 Hadoop配置
同样，将解压后的文件夹重命名为hadoop
在 /etc/profile 文件添加内容 
```
export HADOOP_HOME=usr/lib/hadoop
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
```
修改 /usr/lib/hadoop/etc/hadoop/hadoop-env.sh
```
# The java implementation to use.
export JAVA_HOME=${JAVA_HOME}
```
修改为：
```
# The java implementation to use.
export JAVA_HOME=usr/lib/jdk
```
创建数据文件夹
```
mkdir /usr/hadoop/data
```
修改 /usr/lib/hadoop/etc/hadoop/core-site.xml
```
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://192.168.29.129:9000</value>
  </property>
<!-- 指定hadoop存储数据的目录 -->
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/usr/lib/hadoop/data</value>
  </property>
</configuration>
```
修改 /usr/lib/hadoop/etc/hadoop/hdfs-site.xml
```
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property> 
    <name>dfs.http.address</name> 
    <value>0.0.0.0:50070</value> 
  </property>
</configuration>
```

/usr/lib/hadoop/etc/hadoop/mapred-site.xml
```
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```

/usr/lib/hadoop/etc/hadoop/yarn-site.xml
```
<configuration>
  <!-- Site specific YARN configuration properties -->
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>192.168.29.129</value>
  </property>
  <!-- 分别指定MapReduce的方式 -->
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
</configuration>
```
初始化Hadoop HDFS文件系统：
```
./usr/lib/hadoop/bin/hdfs namenode -format
```
#### 4 Spark安装
```
wget https://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
tar -zxvf spark-2.4.7-bin-hadoop2.7.tgz -C /usr/lib/

```
同样，将解压后的文件夹重命名为spark

```
SPARK_HOME=/usr/lib/spark
PATH=$SPARK_HOME/bin:$PATH
```