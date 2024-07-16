BEGIN;

create table temperature(tm datetime default CURRENT_TIMESTAMP, temperature float not null, humdity float not null, location text);

CREATE INDEX timestamp_ndx ON temperature (tm);
COMMIT;
