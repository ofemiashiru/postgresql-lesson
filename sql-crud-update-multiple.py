# Crud - Update Multiple Recorda and Read

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

# First lets find all the records we want to update
records = session.query(Programmer)

for record in records:
    if record.gender == "Female":
        record.gender = "Fe"
    elif record.gender == "Male":
        record.gender = "Ma"
    else:
        print("Gender not defined")

    # we need to put put our commit at the end if each iteration of the loop
    # or the change will only apply on the last record if it is outside
    session.commit()


# read information from the Programmer table
programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id, programmer.first_name,
          programmer.last_name, programmer.gender, sep=" | ")
