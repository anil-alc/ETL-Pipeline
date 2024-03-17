import pandas as pd
import sqlalchemy as sa

df= pd.read_excel('C:/Users/Anıl Alkan/Desktop/etl_data1.xlsx')
df['FullName']= df['FirstName'] + ' ' + df['LastName'] 
print(df)

engine=sa.create_engine('mssql+pyodbc://./DWH?driver=SQL+Server+Native+Client+11.0')

df.to_sql(name='DimEmployee', con=engine, index=False, if_exists='append')
#df.to_sql(name='DimEmployee', con=engine, index=False, if_exists='fail|append|replace')

print("*")
