# odbc

## Requirements

- Python 3.x
- [pyodbc](https://github.com/mkleehammer/pyodbc)
- [MySQL Community Server 8.0.11](https://dev.mysql.com/downloads/mysql/)
- [MySQL Connector/ODBC 8.0.11](https://dev.mysql.com/downloads/connector/odbc/)

## Docs

- [MySQL Connector/ODBC Doc](https://dev.mysql.com/doc/connector-odbc/en/)
- [pyodbc Doc](https://github.com/mkleehammer/pyodbc/wiki)

## 环境配置

### MacOS

需要先安装[MySQL Community Server 8.0.11](https://dev.mysql.com/downloads/mysql/)和[ODBC Manager](http://www.odbcmanager.net/)，再安装[MySQL Connector/ODBC 8.0.11](https://dev.mysql.com/downloads/connector/odbc/)。

```shell
$ brew install unixodbc

$ odbcinst -j
unixODBC 2.3.6
DRIVERS............: /usr/local/etc/odbcinst.ini
SYSTEM DATA SOURCES: /usr/local/etc/odbc.ini
FILE DATA SOURCES..: /usr/local/etc/ODBCDataSources
USER DATA SOURCES..: /Users/Swiftie_Terrence/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8

$ vim /usr/local/etc/odbcinst.ini

$ cat /usr/local/etc/odbcinst.ini
[MySQL ODBC 8.0 ANSI Driver]
Driver=/usr/local/mysql-connector-odbc-8.0.11-macos10.13-x86-64bit/lib/libmyodbc8a.so
[MySQL ODBC 8.0 Unicode Driver]
Driver=/usr/local/mysql-connector-odbc-8.0.11-macos10.13-x86-64bit/lib/libmyodbc8w.so
```

见`test.py`

### Windows

先下载[MySQL Community Server 8.0.11](https://dev.mysql.com/downloads/mysql/)，下载好后的[安装教程](https://www.jb51.net/article/140957.htm)

接着安装ODBC：在cmd里输入`pip install pyodbc`，等待安装完成就行

最后安装[MySQL Connector/ODBC 8.0.11](https://dev.mysql.com/downloads/connector/odbc/)。

以上就是实验环境的配置，接下来测试`test.py`：

1. 打开cmd，输入`mysql -uroot -p密码`
2. 输入`create database test;`，这是创建数据库test
3. 输入`use test;`，这是修改test数据库
4. `create table S(Sno CHAR(9) PRIMARY KEY,Sname CHAR(20) UNIQUE,Ssex CHAR(2),Sage SMALLINT,Sdept CHAR(20));`

这样子就创建好了一个表，就可以运行`test.py`了，注意`test.py`代码要修改一些东西：

```python
conn = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Ansi Driver};SERVER=127.0.0.1;DATABASE=test;UID=root;PWD=密码')

for row in cursor.execute("desc S"): //这里S是我刚才创建的表S
```

## Reference

[blog](http://www.mranuran.com/blog/2017/08/02/student-database-system-using-pyqt-and-sqlite3/)
