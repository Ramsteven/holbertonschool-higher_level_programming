#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column


if __name__ == "__main__":
    "engine"
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.bind = engine
    Session = sessionmaker()
    Session.bind = engine
    current_session = Session()
    data = current_session.query(State).first()
    if data:
        print("{}: {}".format(data.id, data.name))
    else:
        print("Nothing")
