# like the expression layer we import the modules needed apart from the Table
# one as we are going to be using classes to represent our tablez
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to our specific database location -This tells the application that
# we're using the Postgres server, on a local host since there are 3 slashes,
# in order to connect to our Chinook database.
db = create_engine("postgresql:///chinook")

# Next, we need a variable called 'base', which will be set to the
# declarative_base class. This new 'base' class will essentially grab the
# metadata that is produced by our database table schema.
base = declarative_base()

# create classes that represent each of our tables (class-based model)
# this needs to be created before the session and after the base

# Classes defined in python must be written in PascalCase


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# we do not connect to the database directly instead we ask for session by
# creating a new instance of the session maker and have it point to our db
# variable.
Session = sessionmaker(db)

# however we still need to ACTUALLY open a session, which we do by create an
# instance of the Session which we created above.
session = Session()

# we need to then create the database subclass and generate the meta data
base.metadata.create_all(db)

# create a variable and then use the the .query() method from the session class
# we can then iterate over the results found and print them out

# Query 1 - select all [The sep="" allows us to place separators between items]
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select a specifici column
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select artist where the name is "Queen" - we use the filter_by()
# method to reference the column and the .first() to make sure it only returns
# the first it comes accross just in case there is more than one result
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - filter_by() the ArtistId
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.Name)

# Query 5 - bring back results from Album table where artist is Queen
albums = session.query(Album).filter_by(ArtistId=51)

for album in albums:
    print(f"{album.Title:20} {album.ArtistId}")
