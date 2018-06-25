# odbc
**Requirements**

- Python 3.x
- [pyodbc](https://github.com/mkleehammer/pyodbc)
- [MySQL Community Server 8.0.11](https://dev.mysql.com/downloads/mysql/)
- [MySQL Connector/ODBC 8.0.11](https://dev.mysql.com/downloads/connector/odbc/)

**Docs**

- [MySQL Connector/ODBC Doc](https://dev.mysql.com/doc/connector-odbc/en/)
- [pyodbc Doc](https://github.com/mkleehammer/pyodbc/wiki)

**MacOS**

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

**Linux**