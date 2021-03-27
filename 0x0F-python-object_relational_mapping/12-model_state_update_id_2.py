#!/usr/bin/python3
"""
Start link class to table in database
"""
from sys import argv
from model_state import Base, State
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
    data = current_session.query(State).filter(State.id == 2).first()
    if data:
        data.name = "New Mexico"
        current_session.commit()
    else:
        pass
