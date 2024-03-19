import pandas as pd
import sqlalchemy as sa
import random

"""Import data from excel to MS SQL Server"""
def csv_to_server():
    df= pd.read_excel('C:/Users/Anıl Alkan/Desktop/etl_data.xlsx')
    df['FullName']= df['FirstName'] + ' ' + df['LastName'] 
    print(df)

    engine=sa.create_engine('mssql+pyodbc://./DWH?driver=SQL+Server+Native+Client+11.0')

    try:
        df.to_sql(name='DimEmployee', con=engine, index=False, if_exists='replace')
        #df.to_sql(name='DimEmployee', con=engine, index=False, if_exists='fail|append|replace')

        print("*Data SQL Server'a import edildi.*")
    except:
        print("Import sırasında hata!")


csv_to_server()

"""Export DB from MS SQL Server to Sqlite file"""
def server_to_sqlite():
    engine=sa.create_engine('mssql+pyodbc://./DWH?driver=SQL+Server+Native+Client+11.0')
    
    with engine.connect() as conn, conn.begin():
        data= pd.read_sql_table("DimEmployee",conn)
    #print(data)

    df2=data
    df2.columns = df2.columns.str.strip()
    age=[]

    for i in range(len(df2)):
        age.append(random.randint(29,60))
        
    df2.insert(5, "Age", age, True)
    print(df2)

    sqlite_engine = sa.create_engine("sqlite:///demo.db")

    try:
        df2.to_sql('DimEmployee', con=sqlite_engine, index=False, if_exists='replace')
        #df2.to_sql('DimEmployee', con=sqlite_engine, index=False, if_exists='fail|append|replace')

        print("Sqlite DB export edildi.")
    except:
        print("Export sırasında hata")

    
server_to_sqlite()    
