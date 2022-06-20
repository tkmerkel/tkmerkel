import requests
import pandas as pd
from datetime import datetime, timedelta

#SQL IMPORTS
import csv
from io import StringIO
from sqlalchemy import create_engine

url = 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv'

arkk_data = requests.get(url).text.split('\n')

data = []

for i, line in enumerate(arkk_data):
    data_line = line.split(',')
    if i == 0:
        data_header = data_line
    if len(data_line) < 2:
        continue
    if data_line[1] == 'ARKK':
        data.append(data_line)

df = pd.DataFrame(data)
df.columns = data_header
df = df.rename(columns={'"market value($)"': 'market_value'})
df[['shares', 'market_value', 'weight(%)']] = df[['shares', 'market_value', 'weight(%)']].apply(pd.to_numeric)

data_date = df.iloc[0][0]
data_date = data_date.split('/')
month = int(data_date[0])
day = int(data_date[1])
year = int(data_date[2])

#Copy dataframes over to SQL
def psql_insert_copy(table, conn, keys, data_iter):
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join('"{}"'.format(k) for k in keys)
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)

engine = create_engine('postgresql://Tim:Sluh2005!!post@localhost:5432/Finance')
df.to_sql(f'arkk_{year}_{month}_{day}', engine, if_exists='replace', method=psql_insert_copy)
print(f'arkk_{year}_{month}_{day} table created!')
