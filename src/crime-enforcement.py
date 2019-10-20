# 2015 Structure Tax Value / Assessment -- Reported in 2016
import pandas as pd
from sqlalchemy import create_engine

# Store CSV Into Dataframe
csv_file = "../resources/ca_law_enforcement_by_county.csv"
law_enforcement_df = pd.read_csv(csv_file)
law_enforcement_df.head()

csv_file = "../resources/ca_offenses_by_county.csv"
offensesbycounty_df = pd.read_csv(csv_file)
offensesbycounty_df.head()

# Create New Data With Select Columns
selected_columns = ['county','total_employees','officers','civilians','fips']
enforcement_selected_df = law_enforcement_df[selected_columns].copy()
enforcement_selected_df

selected_columns = ['county','metro/nonmetro','violent_crime','murder', 'rape','rape_legacy','robbery','assault','property_crime','burglary','larceny','vehicle_theft','arson','fips']
offenses_selected_df = offensesbycounty_df[selected_columns].copy()
offenses_selected_df

# Clean DataFrame
# Process by which the "Not A Number" entry was dropped:
# properties_selected.drop(['NaN'], inplace=True)
# to_drop = [NaN]
# properties_selected[~properties_selected['structuretaxvaluedollarcnt'].isin(to_drop)]
# properties_selected.head()


# Connect To Local Database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/etl_project')
print(engine)

# Use Pandas To Load CSV converted DataFrame into database
enforcement_selected_df.to_sql(name='forcebycounty', con=engine, if_exists='replace', index=True, index_label='id')

offenses_selected_df.to_sql(name='offensesbycounty', con=engine, if_exists='replace', index=True, index_label='id')
# Check For Tables
engine.table_names()

# Confirm Data Has Been Added By Querying The properties_table,
# Note: Can also check using pgAdmin
pd.read_sql_query('SELECT * FROM forcebycounty limit 100', con=engine, index_col = 'id').head()
pd.read_sql_query('SELECT * FROM offensesbycounty limit 100', con=engine, index_col = 'id').head()