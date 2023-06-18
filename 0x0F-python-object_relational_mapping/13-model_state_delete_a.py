#!/usr/bin/python3
"""Deletes all State objects that contain the letter a from
the database hbtn_0e_6_usa.
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

    query = session.query(State)
    query.filter(State.name.like('%a%')).delete(synchronize_session='fetch')

    session.commit()
