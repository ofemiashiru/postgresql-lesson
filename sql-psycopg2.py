import psycopg2

# connect to to our database using the connect() method in psycopg2
# We specify the database in double-quotes, but we could include
# additional connection values such as host, username, password, and so on.

# assign it to a variable called connection
connection = psycopg2.connect(database="chinook")

# we need an instance of a cursor object
# A cursor object is another way of saying a 'set' or 'list', similar to an
# 'array' in JavaScript. Essentially, anything that we query from the database
# will become part of this cursor object, and to read that data, we should
# iterate over the cursor using a for -loop, as an example.
cursor = connection.cursor()

# Use queries to select items from the databases tables
# Queries should be in the .execute() method
# queries should be in single quotes and table names should be in double quotes
cursor.execute('SELECT * FROM "Artist"')

# Before we query the database we need to set up a way for the data to be
# retrieved or fetched from the cursor

# for multiple fetch results
results = cursor.fetchall()

# for singular fetch results
# results = cursor.fetchone()

# Next, once our results have been fetched, we need to end the connection
# to the database, so the connection isn't always persistent.
connection.close()

# no we can retrieve each record similarly to how we loop through an array
for result in results:
    print(result)
