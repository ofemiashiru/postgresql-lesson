# Crud - Update Single Record and Read

from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

# Create a brand new table - using the class based model


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)  # this will autoincrement
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

# First lets find the record we want to update
# remember that using the .first() brings back the first matching record
# if you do not use .first() you will need to use a for loop to iterate over
# the results
programmer = session.query(Programmer).filter_by(id=12).first()

# once we have target the specific record we can then programatically state
# what we want to update
programmer.famous_for = "Musician"
programmer.first_name = "James"

# commit the new changes to the record to the table - similar to the git
# commit command
session.commit()


# read information from the Programmer table
programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id, programmer.first_name,
          programmer.last_name, programmer.famous_for, sep=" | ")
