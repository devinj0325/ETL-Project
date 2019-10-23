CREATE DATABASE etl_project;


CREATE TABLE force_by_county
(
    id SERIAL PRIMARY KEY,
    county VARCHAR,
    total_employees INT,
    officers INT,
    civilians INT,
    fips INT
)
;

CREATE TABLE offenses_by_county
(
    id SERIAL PRIMARY KEY,
    county VARCHAR,
    violent_crime INT,
    murder INT,
    rape INT,
    robbery INT,
    assault INT,
    property_crime INT,
    burglary INT,
    fips INT
);


CREATE TABLE property_assessment 
(
    id SERIAL PRIMARY KEY,
    assessment_year INT,
    fips INT,
    structuretaxvaluedollarcnt FLOAT
);


CREATE TABLE square_footage
(
    id SERIAL PRIMARY KEY,
    fips INT,
    assessment_year INT,
    sqaure_footage FLOAT
);

