CREATE TABLE forcebycounty
(
    id SERIAL PRIMARY KEY,
    county VARCHAR,
    total_employees INT,
    officers INT,
    civilians INT,
    fips INT
)
;

SELECT *
FROM forcebycounty;