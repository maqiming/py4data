# 环境准备-Kylin

基于 Hadoop+HBase+Hive

#### 1.1 Hadoop 安装配置
参考 [001-PySpark环境安装-Hadoop安装配置](001_full_install.md#4.1 Hadoop安装)

#### 2.1 HBase 安装
```Shell
wget https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/2.3.2/hbase-2.3.2-bin.tar.gz
tar -zxvf hbase-2.3.2-bin.tar.gz -C /usr/local/
```
#### 2.2 HBase 配置
将解压后的文件夹重命名为hbase方便使用  
在 /etc/profile 文件添加内容
```
export HBASE_HOME=/usr/local/hbase
export PATH=$HBASE_HOME/bin:$PATH
```


#### 3.1 Hive 安装
```Shell
https://mirrors.tuna.tsinghua.edu.cn/apache/hive/hive-2.3.7/apache-hive-2.3.7-bin.tar.gz
tar -zxvf apache-hive-2.3.7-bin.tar.gz -C /usr/local/
```

#### 3.2 Hive 配置
将解压后的文件夹重命名为hive方便使用  
在 /etc/profile 文件添加内容
```
export HIVE_HOME=/usr/local/hive
export HIVE_CONF_HOME=$HIVE_HOME/conf
export HCAT_HOME=$HIVE_HOME/hcatalog
export PATH=$HIVE_HOME/bin:$PATH
```


#### 4.1 Kylin 安装
```Shell
wget https://mirrors.tuna.tsinghua.edu.cn/apache/kylin/apache-kylin-3.1.1/apache-kylin-3.1.1-bin-hbase1x.tar.gz
tar -zxvf apache-kylin-3.1.1-bin-hbase1x.tar.gz -C /usr/local/
```

#### 4.2 Kylin 配置
将解压后的文件夹重命名为kylin方便使用  
在 /etc/profile 文件添加内容
```
export KYLIN_HOME=/usr/local/kylin
export PATH=$KYLIN_HOME/bin:$PATH
```


