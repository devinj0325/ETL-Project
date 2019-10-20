# Crime and Housing Data Analysis | ETL Technical Report
This repository represents an Extract, Transform, and Load (ETL) pipeline for analysis of Housing Data vs. Crime in California by County. The producers of the data are Zillow and the FBI, respectively. We pulled our data from Kaggle in csv format. From there we transformed our data, removing unneeded columns and NaN/null values using Jupyter Notebooks. Next, we loaded them into PostgreSQL via the sqlalchemy and psycopg2 packages. 

## Data Sources
- Kaggle.com

Extract 
-	You will have to create a Kaggle account in order to download the CSV files; you will also need to provide a phone number for mulifactor authentication for the Zillow data
-	Download Zillow CSV file from Kaggle (https://www.kaggle.com/c/zillow-prize-1/data)
-	This data set is too large to store in GitHub, so the file must be stored locally
-	A data dictionary, in excel format, was also downloaded as it defines what the column headers mean
-	File path: resources/Zillow_data_dictionary.xlsx
-	Download Crime CSV files from Kaggle (https://www.kaggle.com/fbi-us/california-crime#ca_offenses_by_city.csv)
-	The Crime data file paths are: resources/ca_law_enforcement_by_county.csv, resources/ca_offenses_by_county.csv


Transformation
-	Read the csv file in Jupyter Notebook
-	Note: FIPS is the Federal Information Processing Standard to uniquely identify counties in the United States. We used FIPS as a way to ensure our datasets were relational and easy to join. 
-	For the assessment of housing data and square footage:
    -	Filter columns (“calculated_square_feet”, “asessment_year”, “fips”)
    -	Dropped any NaN’s in the “calculated_square_feet” column
-	For property tax assessments:
    -	Filtered columns (“id”, “assessment_year”, “structure_tax_value_dollar_cnt”, “fips”) reducing from 58 columns to 4 columns
    -	Dropped NaNs in the “structure_tax_value_dollar_cnt” column, reducing from 1,048,576 rows to 1,033,159 rows
-	For the police force size for each of the counties
    -	Filtered columns ("county", "total_employees", "officers", "civilians")
    -	Eliminated all rows except for the counties we are comparing
    -	Added a column for the "fips" code for each county
-	For the offenses for each of the counties    
    -	Filtered columns ('county','violent_crime', 'murder', 'rape', 'robbery','assault','property_crime','burglary','larceny','vehicle_theft','arson', 'fips')
    -	Eliminated all rows except for the counties we are comparing
    -	Added a column for the "fips" code for each county


Load 
-	Created schema 
-	File path: schema/schema.sql
-	Using sqlalchemy and psycopg2, an engine was created, and the CSV files were loaded into PostgreSQL. The table was previously created in PostgreSQL, using our schema. 

### Recommended Queries
**SELECT** square_footage.fips, square_footage.square_footage, offenses_by_county.violent_crime, offenses_by_county.rape
**FROM** offenses_by_county
**INNER JOIN** square_footage 
**ON** square_footage.fips = offenses_by_county.fips
