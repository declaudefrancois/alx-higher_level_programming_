#!/usr/bin/python3
"""Lists all Cities objects from the database hbtn_0e_6_usa.
"""
if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, relationship
    import sys

    State.cities = relationship(
                "City",
                order_by=City.id,
                back_populates="state"
            )
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

    for row in session.query(State).all():
        for city in row.cities:
            print("{}: ({}) {}".format(row.name, city.id, city.name))
