# Data Types
## Character Data
- Character data can be stored as either **fixed-length or variable-length strings**; the difference is that fixed-length strings are right-padded with spaces and always consume
the same number of bytes, and variable-length strings are not right-padded with
spaces and don’t always consume the same number of bytes.

```sql
char(20) /* fixed-length string, right-padded with spaces, always consumes 20 bytes */
varchar(20) /* variable-length string, not right-padded with spaces */
```

- If you need to store longer strings (such as emails, XML documents, etc.), then you will want to use one of the text types (mediumtext
and longtext).

-  To choose
a character set other than the default when defining a column, simply name one of
the supported character sets after the type definition, as in:

```sql
varchar(20) character set utf8mb4
```
### text types

- If you need to store data that might exceed the 64 KB limit for varchar columns, you
will need to use one of the text types.

![alt text](screenshots/ch_2_1.png)

## numeric Data
- different interger types:

![alt text](screenshots/ch_2_2.png)


- floating point types:

    - When using a floating-point type, you can specify a precision (the total number of
allowable digits both to the left and to the right of the decimal point) and a scale (the
number of allowable digits to the right of the decimal point), but they are not
required. 

![alt text](screenshots/ch_2_3.png)

## temporal data

![alt text](screenshots/ch_2_4.png)
![alt text](screenshots/ch_2_5.png)

![alt text](screenshots/ch_2_6.png)

- a timestamp column will automatically be populated with the current date/time by the MySQL server when a row is added to a table or when a row is later modified.

# Table creation

```sql
CREATE TABLE person
(person_id SMALLINT UNSIGNED,
fname VARCHAR(20),
lname VARCHAR(20),
eye_color CHAR(2),
birth_date DATE,
street VARCHAR(30),
city VARCHAR(20),
state VARCHAR(20),
country VARCHAR(20),
postal_code VARCHAR(20),
CONSTRAINT pk_person PRIMARY KEY (person_id)
);
```
- MySQL allows a check constraint to be attached to a column
definition, as in the following:

```sql
eye_color CHAR(2) CHECK (eye_color IN ('BR','BL','GR')),
```

- MySQL does provide another character data type called enum that merges the check
constraint into the data type definition:

```sql
eye_color ENUM('BR','BL','GR'),
```

- check description of a table:

```sql
DESCRIBE person;
```
or

```sql
desc person;
```

- table with foriegn key constraint:

```sql
CREATE TABLE favorite_food
 (person_id SMALLINT UNSIGNED,
 food VARCHAR(20),
 CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
 CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id)
 REFERENCES person (person_id)
 );
```
# Populating and modifying tables
## inserting data
- alter a primary key column to auto increment:

```sql
ALTER TABLE person MODIFY person_id SMALLINT UNSIGNED AUTO_INCREMENT;
```