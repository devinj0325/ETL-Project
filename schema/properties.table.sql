DROP TABLE properties_selected;
CREATE TABLE properties_selected (
id SERIAL PRIMARY KEY,
assessment_year INT,
fips INT,
structuretaxvaluedollarcnt FLOAT
);
