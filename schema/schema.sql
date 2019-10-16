CREATE DATABASE etl_project;

CREATE TABLE forcebycounty
(
    id SERIAL
    county VARCHAR,
    total_employees INT,
    officers INT,
    civilians INT,
    fips INT,
    CONSTRAINT forcebycounty_pkey PRIMARY KEY (id)
)
;
CREATE TABLE offensesbycounty
(
    id SERIAL,
    county VARCHAR,
    

)
