#!/usr/bin/python3
"""
A python script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, password, db_name), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to filter States that contain letter a
    query = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    # Print results
    for state in query:
        print("{}: {}".format(state.id, state.name))
