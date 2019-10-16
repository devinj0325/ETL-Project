CREATE DATABASE etl_project;

CREATE TABLE forcebycounty
(
    id SERIAL
    county VARCHAR,
    total_employees INT,
    officers INT,
    civilians INT
    CONSTRAINT forcebycounty_pkey PRIMARY KEY (id)
)
;

