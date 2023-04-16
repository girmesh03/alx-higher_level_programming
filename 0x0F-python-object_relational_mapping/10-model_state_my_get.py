#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    # Create connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the state with the name passed as argument
    state_name = sys.argv[4]
    state = session.query(State).filter_by(name=state_name).first()

    # Print the state id or "Not found" if there's no matching state
    if state is None:
        print("Not found")
    else:
        print(state.id)
