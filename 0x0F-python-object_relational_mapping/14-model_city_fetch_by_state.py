#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa:
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create an engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # work with sess
    for city, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # close session
    session.close()
