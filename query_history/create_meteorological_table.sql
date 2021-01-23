CREATE TABLE IF NOT EXISTS meteorological (
	measurement_id serial PRIMARY KEY,
	station_id INTEGER,
	measurement_ts TIMESTAMP WITH TIME ZONE UNIQUE NOT NULL,
	-- Zenith Angle [degrees]
	zenith_angle REAL,
	-- Zenith Angle [degrees]
	azimuth_angle REAL,
	airmass REAL,
	-- Tower Dry Bulb Temp [deg C]
	tower_dry_bulb_temp REAL,
	-- Deck Dry Bulb Temp [deg C]
	deck_dry_bulb_temp REAL,
	-- Tower Relative Humidity [%]
	tower_rh REAL,
	-- Deck Relative Humidity [%]
	deck_rh REAL,
	-- Total Cloud Cover [%]
	total_cloud_cover REAL,
	-- Opaque Cloud Cover [%]
	opaque_cloud_cover REAL,
	-- Avg Wind Speed @ 6ft [m/s]
	avg_wind_speed_6ft REAL,
	-- Avg Wind Speed @ 19ft [m/s]
	avg_wind_speed_19ft REAL,
	-- Avg Wind Speed @ 22ft [m/s]
	avg_wind_speed_22ft REAL,
	-- Avg Wind Speed @ 33ft [m/s]
	avg_wind_speed_33ft REAL,
	-- Avg Wind Direction @ 6ft [deg from N]
	avg_wind_direction_6ft REAL,
	-- Avg Wind Direction @ 19ft [deg from N]
	avg_wind_direction_19ft REAL,
	-- Avg Wind Direction @ 22ft [deg from N]
	avg_wind_direction_22ft REAL,
	-- Avg Wind Direction @ 33ft [deg from N]
	avg_wind_direction_33ft REAL,
	-- Vertical Wind Shear [1/s]
	vertical_wind_shear REAL,
	-- Station Pressure [mBar]
	station_pressure REAL,
	-- Precipitation [mm]
	precipitation REAL,
	-- Albedo (LI-200)
	albedo REAL,
	-- Albedo Quantum (LI-190)
	albedo_quantum REAL
);

ALTER TABLE meteorological
	ADD CONSTRAINT fk_station
			FOREIGN KEY ( station_id )
				REFERENCES stations ( station_id );