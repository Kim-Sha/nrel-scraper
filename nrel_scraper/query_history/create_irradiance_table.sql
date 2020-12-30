CREATE TABLE IF NOT EXISTS irradiance (
	measurement_id serial PRIMARY KEY,
	station_id INTEGER,
	measurement_ts TIMESTAMP WITH TIME ZONE UNIQUE NOT NULL,
	global_psp REAL,
	global_li200 REAL,
	global_40_south_cmp22 REAL,
	global_40_south_li200r REAL,
	global_90_north_psp REAL,
	global_90_north_li200 REAL,
	global_90_east_psp REAL,
	global_90_east_li200 REAL,
	global_90_south_psp REAL,
	global_90_south_li200 REAL,
	global_90_west_psp REAL,
	global_90_west_li200 REAL,
	global_normal_cmp22 REAL,
	global_normal_li200r REAL,
	direct_nip REAL,
	direct_snip REAL,
	diffuse_cm22_1 REAL,
	diffuse_cm22_2 REAL
);

ALTER TABLE irradiance
	ADD CONSTRAINT fk_station
			FOREIGN KEY ( station_id )
				REFERENCES stations ( station_id );