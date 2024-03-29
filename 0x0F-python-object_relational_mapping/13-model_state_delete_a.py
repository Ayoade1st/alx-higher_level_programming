#!/usr/bin/python3
'''
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
'''
import sys
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state_name = session.query(State).filter(
            State.name.like("%a%")).all()
        for state in state_name:
            session.delete(state)
            session.commit()
