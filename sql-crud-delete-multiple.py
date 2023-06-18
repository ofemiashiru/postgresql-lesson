# Crud - Delete Multiple Records and Read

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

# DO NOT RUN THIS - this would be the way to delete multiple records
# When using this make sure to use defensive program to confirm deletion

records = session.query(Programmer)
confirmation = input('Are you sure you want to delete all records? (y/n) ')

if confirmation.lower() == 'y':

    for record in records:
        session.delete(record)
        session.commit()

    print('All records deleted.')

else:
    print('No records have been deleted.')

# read information from the Programmer table
programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id, programmer.first_name,
          programmer.last_name, programmer.famous_for, sep=" | ")
