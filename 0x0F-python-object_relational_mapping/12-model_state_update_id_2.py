#!/usr/bin/python3
"""changes the name of a State object"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an instance of the engine for connecting to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory using sessionmaker
    Session = sessionmaker(bind=engine)

    # Create a session object using the session factory
    session = Session()

    # Query the State object where id = 2
    state = session.query(State).filter_by(id=2).first()

    # Change the name of the State object
    state.name = "New Mexico"

    # Add the modified State object to the session
    session.add(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
