# Postgres SQL database cheatsheet

#### See a list of databases on the server

type the backslash el command

```
 postgres#$ \l
```

#### Connect to a database

```
 postgres#$ \c <name of DB>
```
Or connect directly fromthe command prompt

```
 $ psql -h localhost -p 5432 -U postgres <name of DB>
```


#### Create tables / view tables

```sql
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);

```
To see a list of tables or to query a table structure

```
  postgres#$ \d <table name optional>
```

To connect to a database using prisma you need the connection string:

![image](https://user-images.githubusercontent.com/8973660/201624874-942fcf88-7356-4cb2-9f4b-f5ba03024ea3.png)

