#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get the arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_user, mysql_password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session object
    session = Session()

    # Create the new State object
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the transaction
    session.commit()

    # Print the new state's id
    print(new_state.id)
