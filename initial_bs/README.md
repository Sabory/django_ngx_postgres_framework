# binance_hunt
docker-compose up -d

docker exec -it binance-db /bin/bash

psql --username=taco

CREATE DATABASE binance;

CREATE TABLE binance.table_name(
    id SERIAL,
    timestamp TIMESTAMP NOT NULL,
    open FLOAT8 NOT NULL,
    high FLOAT8 NOT NULL,
    low FLOAT8 NOT NULL,
    close FLOAT8 NOT NULL,
    volume INT8 NOT NULL,
    close_time TIMESTAMP NOT NULL,
    quote_av FLOAT8 NOT NULL,
    trades INT8 NOT NULL,
    tb_base_av FLOAT8 NOT NULL,
    tb_quote_av FLOAT8 NOT NULL,
    ignore FLOAT8 NOT NULL
);