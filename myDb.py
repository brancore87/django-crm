import psycopg
 

#establishing the connection
conn = psycopg.connect(
   user='postgres', password='sangma12', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''
      CREATE DATABASE mydb;
      CREATE USER myprojectuser WITH PASSWORD 'password';
      ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
      ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
      ALTER ROLE myprojectuser SET timezone TO 'Asia/Kolkata';
      GRANT ALL PRIVILEGES ON DATABASE mydb TO myprojectuser;

'''

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()