# Crime and Housing Data Analysis | ETL Technical Report
This repository represents an Extract, Transform, and Load (ETL) pipeline for analysis of Housing Data (Zillow) vs. Crime in California by County. Our Data is from Kaggle in csv format. From there we transformed our Zillow data and Crime data, reducing the number of unneeded columns (We came across quite a number of NaN/null values) and also removing repetitive columns using Jupyter Notebooks. Next, we loaded them out to PostgreSQL via the sqlalchemy and psycopg2 packages. 

Extract 
-	Downloaded Zillow CSV file from Kaggle (https://www.kaggle.com/c/zillow-prize-1/data)
- Downloaded Crime CSV files from Kaggle (https://www.kaggle.com/fbi-us/california-crime#ca_offenses_by_city.csv)
-	File path  resources/Zillow_Data_2015.csv & ca_law_enforcement_by_county.csv, ca_offenses_by_county.csv
-	You will have to create a Kaggle account in order to download the CSV files
-	A dictionary, in excel format, was also downloaded as it defines what the column headers mean
-	File path  resources/Zillow_data_dictionary.xlsx

Transformation
-	Read the csv file in Jupyter Notebook
-	Filter columns (“calculated_square_feet”, “asessment_year”, “fips”)
-	Filtered columns (“id”, “assessment_year”, “structure_tax_value_dollar_cnt”, “’fips”) reducing from 58 columns to 4 columns
-	FIPS is the Federal Information Processing Standard to uniquely identify counties in the United States. We used FIPS as a way to ensure our datasets were relational and easy to join. 
-	Dropped any NaN’s in the “calculated_square_feet” column
-	Dropped NaNs in the “structure_tax_value_dollar_cnt” column, reducing from 1,048,576 rows to 1,033,159 rows

Load 
-	Created schema 
o	File path  schema/squarefootage.sql
-	Using sqlalchemy and psycopg2, an engine was created, and the CSV files were loaded into PostgreSQL. The table was previously created in PostgreSQL, using our schema. 

Queries
SELECT square_footage.fips, square_footage.square_footage, offensesbycounty.violent_crime, offensesbycounty.rape
FROM offensesbycounty
INNER JOIN square_footage ON
square_footage.fips = offensesbycounty.fips
