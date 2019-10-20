# 2015 Structure Tax Value / Assessment -- Reported in 2016
import pandas as pd
from sqlalchemy import create_engine

# Store CSV Into Dataframe
csv_file = "./Resources/properties_2016.csv"
properties_2016_df = pd.read_csv(csv_file)
properties_2016_df.head()

# Create New Data With Select Columns
selected_columns = ['assessmentyear', 'fips', 'structuretaxvaluedollarcnt']
properties_selected_df = properties_2016_df[selected_columns].copy()
properties_selected_df

properties_selected_df.dropna(how='any', inplace=True)
properties_selected_df

# Connect To Local Database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/properties_selected_db')
print(engine)

# Use Pandas To Load CSV converted DataFrame into database
properties_selected_df.to_sql(name='properties_table', con=engine, if_exists='replace', index=True, index_label='id')

# Check For Tables
engine.table_names()

# Confirm Data Has Been Added By Querying The properties_table,
# Note: Can also check using pgAdmin
pd.read_sql_query('SELECT * FROM properties_table limit 100', con=engine, index_col = 'id').head()

