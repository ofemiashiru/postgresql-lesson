# import modules from sqlalchemy
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData,
    select
)

# executing the instructions from our localhost  "chinook" db
# we use create_engine() to connect and store it in a variable called db
# the 3 slashes indicate that the database is hosted locally within our
# workspace environment
db = create_engine('postgresql:///chinook')

# data about our tables and the data about the data within those tables
meta = MetaData(db)


# create variable for each of our tables that match the schema or
# database model
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    # when defining columns that are foreign keys that we do not need
    # set the primary_key property to false
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    # set UnitPrice to float as it uses decimal values for price
    Column("UnitPrice", Float)

)

# make a connection to the database using the python with statement (opens and
# closes the connection for us) and store it in a variable called connection

with db.connect() as connection:

    # query 1 - selecting all from artist table
    # select_query = artist_table.select()

    # query 2 - select specific columns using the with_only_columns() method
    # and using .c to identify the specific column we want to return
    # select_query = artist_table.select().with_only_columns([
    #     artist_table.c.Name
    # ])

    # query 3 select values using the WHERE clause
    # select_query =artist_table.select().where(artist_table.c.Name == "Queen")

    # query 4 similar to query 3 however we are looking at an id
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 5 - looking within a different table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 6 - select specific columns - import select module above and then
    # use select(column, column)
    select_query = select(track_table.c.Name, track_table.c.UnitPrice).where(
        track_table.c.Composer == 'Queen')

    results = connection.execute(select_query)

    for result in results:
        print(result)
