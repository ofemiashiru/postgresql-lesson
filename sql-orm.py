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
db = create_engine("postgres:///chinook")

# Next, we need a variable called 'base', which will be set to the
# declarative_base() class. This new 'base' class will essentially grab the
# metadata that is produced by our database table schema.
base = declarative_base()

# create classes that represent each of our tables (class-based model)
# this needs to be created before the session and after the base

# Classes defined in python must be written in PascalCase


class Artitst(base):
    __tablename__ = "Artitst"
    ArtistId = Column(Integer, primary_key=True)
    Artist = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artitst.ArtistId"))


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

