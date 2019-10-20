# California Crime and Law Enforcement data 2015
import pandas as pd
from sqlalchemy import create_engine

# Police Force Data
# Store CSV Into Dataframe
csv_file = "../resources/ca_law_enforcement_by_county.csv"
force_df = pd.read_csv(csv_file)
force_df.head()

#Clean Data
# Remove Metro/NonMetro column
cleaner = force_df.drop('Metropolitan/Nonmetropolitan', axis=1)

#Extract only the 3 counties needed
county_list = ['Los Angeles', 'Ventura', 'Orange']
cleaned = cleaner[cleaner['County'].isin(county_list)].copy()

# Setting values for FIPS LA, Orange, Ventura and insert into DataFrame
fips = [6037, 6059, 6111]
cleaned['FIPS'] = fips

#Rename columns
cleaned.columns = ['county', 'total_employees', 'officers', 'civilians', 'fips']

#Remove commas from number fields
cleaned["total_employees"] = pd.to_numeric(cleaned["total_employees"].map(lambda x: x.replace(",", "")))
cleaned["officers"] = pd.to_numeric(cleaned["officers"].map(lambda x: x.replace(",", "")))
cleaned["civilians"] = pd.to_numeric(cleaned["civilians"].map(lambda x: x.replace(",", "")))


# selected_columns = ['county', 'metro/nonmetro','violent_crime', 'murder', 'rape','rape_legacy','robbery','assault','property_crime','burglary','larceny','vehicle_theft','arson', 'fips']
# offenses_selected_df = offensesbycounty_df[selected_columns].copy()
# offenses_selected_df

#Offenses Data
# Store CSV Into Dataframe
csv_file = "../resources/ca_offenses_by_county.csv"
offensesbycounty_df = pd.read_csv(csv_file)
offensesbycounty_df.head()

#Clean Data
# Remove Metro/NonMetro column
offense_df = offensesbycounty_df.drop(["Metropolitan/Nonmetropolitan", "Rape(legacy definition)"], axis=1)
#Extract only the 3 counties needed
counties_list = ['Los Angeles', 'Ventura', 'Orange']
county = offense_df[offense_df['County'].isin(counties_list)].copy()

# Setting values for FIPS LA, Orange, Ventura and insert into DataFrame
county['FIPS'] = fips

#rename columns
county.columns = ['county','violent_crime', 'murder', 'rape', 'robbery','assault','property_crime','burglary','larceny','vehicle_theft','arson', 'fips']

#remove commas from number fields in offense table
county['violent_crime'] = pd.to_numeric(county['violent_crime'].map(lambda x: x.replace(",", "")))

county["robbery"] = pd.to_numeric(county["robbery"].map(lambda x: x.replace(",", "")))

county["property_crime"] = pd.to_numeric(county["property_crime"].map(lambda x: x.replace(",", "")))

county["burglary"] = pd.to_numeric(county["burglary"].map(lambda x: x.replace(",", "")))

county["larceny"] = pd.to_numeric(county["larceny"].map(lambda x: x.replace(",", "")))

county["vehicle_theft"] = pd.to_numeric(county["vehicle_theft"].map(lambda x: x.replace(",", "")))

county["assault"] = pd.to_numeric(county["assault"].map(lambda x: x.replace(",", "")))
# Connect To Local Database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/etl_project')
print(engine)

# Use Pandas To Load CSV converted DataFrame into database
cleaned.to_sql(name='force_by_county', con=engine, if_exists='replace', index=True, index_label='id')
cleaned.to_sql(name='offenses_by_county', con=engine, if_exists='replace', index=True, index_label='id')


# offenses_selected_df.to_sql(name='offensesbycounty', con=engine, if_exists='replace', index=True, index_label='id')
# Check For Tables
# engine.table_names()

# Confirm Data Has Been Added By Querying The properties_table,
# Note: Can also check using pgAdmin
# pd.read_sql_query('SELECT * FROM forcebycounty limit 100', con=engine, index_col = 'id').head()
# pd.read_sql_query('SELECT * FROM offensesbycounty limit 100', con=engine, index_col = 'id').head()