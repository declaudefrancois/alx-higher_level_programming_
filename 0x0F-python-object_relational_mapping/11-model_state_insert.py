#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa using
   the State class.
"""
if __name__ == "__main__":
    from model_state import Base, State
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

    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print("{}".format(state.id))
