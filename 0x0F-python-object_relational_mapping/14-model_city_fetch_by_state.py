#!/usr/bin/python3
"""All states via SQLAlchemy.
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    argv[1],
                    argv[2],
                    argv[3]
                ),
                pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State, City).filter(
        State.id == City.state_id
    ).order_by(City.id.asc()).all()

    for row in rows:
        state, city = row
        print("{}: ({}) {}".format(state.name, city.id, city.name))
