# 环境准备-Airflow

#### 1.1 Airflow安装
```shell script
pip3 install apache-airflow -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

#### 1.2 Airflow配置 

export PATH=~/.local/bin:$PATH

在 /etc/profile 文件添加内容   
```
echo "export AIRFLOW_HOME=/home/airflow" >> /etc/profile
source /etc/profile
```

使前述各项配置立即生效
```

```