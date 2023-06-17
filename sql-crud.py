# Crud - Create and Read

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


# Create new record in our Programmer table - we do this be creating a variable
# pointing to the class and using key value pairs to create the record
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

magaret_hamilton = Programmer(
    first_name="Magaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

femi_ash = Programmer(
    first_name="Femi",
    last_name="Ash",
    gender="M",
    nationality="Nigerian",
    famous_for="Aspiring Full Stack Developer"
)

# add the newly created record - similar to git command adding to staging
# remember to comment out the session.add() you have already done as it will
# add a second record
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(magaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
session.add(femi_ash)

# commit the new record(s) to the table - similar to the git commit command
session.commit()


programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer.id, programmer.first_name,
          programmer.last_name, sep=" | ")
