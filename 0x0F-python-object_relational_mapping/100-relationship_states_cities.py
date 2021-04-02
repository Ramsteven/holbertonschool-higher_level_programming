#!/usr/bin/python3
"""relationship states cities"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]
    db = argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, pwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name='California')
    new_state.cities = [City(name='San Francisco')]

    session.add(new_state)
    session.commit()
    session.close()
