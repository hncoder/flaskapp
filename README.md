# flaskapp
a flask app development architecture

## 1）服务器准备

安装python3  
centos:  
https://www.cnblogs.com/JahanGu/p/7452527.html

mac:
方法一：https://www.python.org  
方法二：brew install python3  

安装pip3  
centos:
https://www.cnblogs.com/wenchengxiaopenyou/p/5709218.html

安装flask：pip3 install flask

安装Pymysql: pip3 install PyMySQL


安装数据库  
centos:
https://www.cnblogs.com/starof/p/4680083.html

mac:
https://dev.mysql.com/downloads/mysql/  
配置环境变量：export PATH=${PATH}:/usr/local/mysql/bin  
启动数据库：系统偏好设置  
连接mysql：mysql -u root -p  
修改root密码：ALTER USER 'root'@'localhost' IDENTIFIED BY 'root'  
mac mysql可视化工具：Workbench  
卸载mysql：sudo rm -rf /var/db/receipts/com.mysql.*  
远程连接：http://blog.csdn.net/freecodetor/article/details/5799550

安装虚拟环境  
sudo easy_install virtualenv  

安装flask  
pip3 install flask  

安装nginx  
http://www.linuxidc.com/Linux/2016-09/134907.htm

安装开发工具及插件  
sublime3  

## 2）开发准备  
修改名称  

创建虚拟环境  
virtualenv venv  
source venv/bin/activate   

安装flask扩展框架  
pip3 freeze >requirements.txt  
pip3 install -r requirements.txt  

数据库配置  

数据库迁移初始化  
python3 manage.py db init  

数据库迁移  
python3 manage.py db migrate -m "xxxx"  
python3 manage.py db upgrade  
python3 manage.py db downgrade  

## 3）部署  
scp -r app/* root@111.230.223.219:../home/www/kaokeapp/app/
https://www.cnblogs.com/Ray-liang/p/4837850.html
