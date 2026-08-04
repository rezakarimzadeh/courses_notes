link to the course: [link](https://www.youtube.com/playlist?list=PL7D4X4pSOcCGoKVKDNjeKLRDK4TNRxc1x)

## create a table and insert entries into it

```sql
 CREATE TABLE cities (
   name VARCHAR(50),
   country VARCHAR(50),
   population INTEGER,
   area INTEGER
 );

 INSERT INTO cities (name, country, population, area)
 VALUES 
    ('Tokyo', 'Japan', 38505000, 8223),
   ('Delhi', 'India', 28125000, 2240),
   ('Shanghai', 'China', 22125000, 4015),
   ('Sao Paulo', 'Brazil', 20935000, 3043);
```

## select all data from the table

```sql
SELECT * FROM cities;
```

## select specific columns from the table

```sql
SELECT name, country FROM cities;
```

## Do calculations on the data

```sql
SELECT name, population / area AS population_density FROM cities;
```

## Use functions to manipulate the data

```sql
select concat(UPPER(name), ', ', UPER(country)) AS location from cities;
```

## make a table with primary key

```sql
CREATE TABLE users (
	id SERIAL primary key,
	username varchar(50)
);
```

## conditional row selection

```sql
SELECT * FROM cities WHERE population > 20000000;
```

## join corresponding rows from multiple tables

```sql
select * from photos JOIN users on users.id = photos.user_id;
```



