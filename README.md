# odbc

## Requirements

- PHP 7.1
- [MySQL Community Server 8.0.11](https://dev.mysql.com/downloads/mysql/)
- [MySQL Connector/ODBC 8.0.11](https://dev.mysql.com/downloads/connector/odbc/)

## Docs

- [MySQL Connector/ODBC Doc](https://dev.mysql.com/doc/connector-odbc/en/)

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

$ vim /usr/local/etc/odbc.ini

$ cat /usr/local/etc/odbc.ini
[MySQLServer]
Driver = MySQL ODBC 8.0 ANSI Driver
Server = 127.0.0.1
Port = 3306
Database = test
Charset = utf8
```

### Windows

先下载[MySQL Community Server 8.0.11](https://dev.mysql.com/downloads/mysql/)，下载好后的[安装教程](https://www.jb51.net/article/140957.htm)

## TODO

- 爱好 改成中文
- 正则匹配检验完整性
- 不上传头像使用一张默认图片作为头像
- cookie