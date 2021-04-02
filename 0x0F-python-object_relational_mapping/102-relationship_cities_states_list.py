#!/usr/bin/python3
"""relationship states cities list"""
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

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
