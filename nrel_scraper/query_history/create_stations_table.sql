CREATE TABLE IF NOT EXISTS stations (
    station_id serial PRIMARY KEY,
    station_name VARCHAR ( 100 ) UNIQUE NOT NULL,
    coordinates POINT
);