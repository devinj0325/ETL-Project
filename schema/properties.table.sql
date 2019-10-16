DROP TABLE properties_selected;
CREATE TABLE properties_selected (
id INT PRIMARY KEY,
assessment_year INT,
fips TEXT,
structuretaxvaluedollarcnt FLOAT
);

SELECT * FROM
