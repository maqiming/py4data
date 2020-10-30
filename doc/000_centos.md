# CentOS 基础配置

#### 0 如果新机器非硬件原因无网络
查看网卡
```shell script
ip addr
vi /etc/sysconfig/network-scripts/ifcfg-网卡名
修改 ONBOOT=no 为 ONBOOT=yes
```
#### 1.1 安装ifconfig
```shell script
yum search ifconfig
yum install net-tools.x86_64
```
#### 1.2 安装wget
```shell script
yum install wget
```
#### 1.3 允许 ssh远程登陆
```shell script
vi /etc/ssh/sshd_config
```
取消部分配置项前的注释
```shell script
Port 22
PermitRootLogin yes
PasswordAuthentication yes
```