#! /bin/bash
mysql --user="root" --password="123" --execute="CREATE DATABASE IF NOT EXISTS management;
USE management;
CREATE TABLE IF NOT EXISTS user (
        id_user int NOT NULL PRIMARY KEY,
        name varchar(100),
        gender char(1),
        dt_birth date,
        cep varchar(10),
        street varchar(100),
        complement varchar(100),
        neighborhood varchar(100),
        city varchar(100),
        state char(2)
);
"
