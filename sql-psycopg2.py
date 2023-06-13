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
# QUERY 1 - All values from a table
# cursor.execute('SELECT * FROM "Artist"')

# QUERY 2 - Select specific column from a table
# cursor.execute('SELECT "Name" FROM "Artist"')

# QUERY 3 - Specific value -combination of single and double quotes do not work
# We need to use a Python string placeholder, and then define the desired
# string within a list.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# QUERY 4 - is similar to the above except we us an integer in the list
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# QUERY 5 - getting Albums with the same ArtistId as above
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# QUERY 6 - getting all tracks where the composer is Queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# QUERY 7 - find some values on my own - if we change the value to one that is
# not present in the table an exception will be raised stating that that
# TypeError:'NoneType' object is not iterable
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Aerosmith"])

# Before we query the database we need to set up a way for the data to be
# retrieved or fetched from the cursor

# for multiple fetch results
# results = cursor.fetchall()

# for singular fetch results
results = cursor.fetchone()

# Next, once our results have been fetched, we need to end the connection
# to the database, so the connection isn't always persistent.
connection.close()

# no we can retrieve each record similarly to how we loop through an array
for result in results:
    print(result)
