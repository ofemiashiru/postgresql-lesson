# Crud - Delete Single Record and Read

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

# To make it more interactive we can prompt a user to give a specific user to
# delete

fname = input("Enter the first name: ")
lname = input("Enter the last name: ")

# Use the input given from the user to programaticaly search and delete record
# remember that using the .first() brings back the first matching record
# if you do not use .first() you will need to use a for loop to iterate over
# the results
programmer = session.query(Programmer).filter_by(
    first_name=fname,
    last_name=lname
).first()

programmer = session.query(Programmer).filter_by(
    first_name=fname, last_name=lname).first()

# Defensive programming to check if the programmer entered exists
if programmer is not None:
    print(f'User {programmer.first_name} {programmer.last_name} found')
    confirmation = input(
        "Are you sure you want to delete this record? (y/n) "
    )
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()   # commit used to commit the relevant changes
        print("Record deleted")
    else:
        print("Programmer not deleted")

else:
    print('No records found')

# read information from the Programmer table
programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id, programmer.first_name,
          programmer.last_name, programmer.famous_for, sep=" | ")
