#!/usr/bin/python3
"""Start link class to table in database 
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column


if __name__ == "__main__":
    "engine"
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.bind = engine
    Session = sessionmaker()
    Session.bind = engine
    current_session = Session() 
    data = current_session.query(State, City).filter(State.id == City.state_id).all()

    for city in data:
        print("{}: ({}) {}".format(
            item.State.name,
            item.City.id,
            item.City.name
        ))    
