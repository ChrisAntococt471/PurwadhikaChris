import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345',
    database='world'
)

mycursor=mydb.cursor()
query='select * from city'
mycursor.execute(query)
result=mycursor.fetchall()
df=pd.DataFrame(result,columns=mycursor.column_names)
df.head(5)