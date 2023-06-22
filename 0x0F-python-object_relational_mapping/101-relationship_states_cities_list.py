#!/usr/bin/python3
"""ists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
if __name__ == "__main__":
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    sys.argv[1],
                    sys.argv[2],
                    sys.argv[3]
                ),
                pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    # Create a session.
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).join(State.cities).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
