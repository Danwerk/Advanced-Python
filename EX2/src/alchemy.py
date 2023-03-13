from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///../database/DINERS2.db', echo=False)
meta = MetaData()
Base = declarative_base()


class Provider(Base):
    """Class for the providers table."""
    __tablename__ = 'providers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    provider_name = Column(String, unique=True)


class Canteen(Base):
    """Class for the canteens table."""
    __tablename__ = 'canteens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    time_open = Column(String)
    time_closed = Column(String)
    provider_id = Column(Integer, ForeignKey('providers.id'))
    provider = relationship("Provider", back_populates="canteens")


# Add a new property canteens to provider and declare relationship
Provider.canteens = relationship("Canteen", order_by=Canteen.id, back_populates="provider")

# Start a session
Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    """Creates tables Provider and Canteen from base."""
    Base.metadata.create_all(engine)


def add_it_college():
    """Add IT College canteen and provider data as separate statement"""
    try:
        session.add(Provider(provider_name="bitStop", canteens=[Canteen(name="bitStop KOHVIK",
                                                                        location="IT college, Raja 4C",
                                                                        time_open="2023-01-01 09:30",
                                                                        time_closed="2023-01-01 16:00")]))
        session.commit()
    except:
        session.rollback()
        raise


def add_other_providers_and_canteens():
    """Add other University canteens and providers data."""
    try:
        session.add_all([Provider(provider_name="Rahva Toit",
                                  canteens=[Canteen(name="Economics- and social science building canteen",
                                                    location="Akadeemia tee 3 SOC- building",
                                                    time_open="2023-01-01 08:30",
                                                    time_closed="2023-01-01 18:30"),
                                            Canteen(name="Libary canteen",
                                                    location="Akadeemia tee 1/Ehitajate tee 7",
                                                    time_open="2023-01-01 08:30",
                                                    time_closed="2023-01-01 19:00"),
                                            Canteen(name="U06 building canteen",
                                                    location="",
                                                    time_open="2023-01-01 09:00",
                                                    time_closed="2023-01-01 16:00")]),
                         Provider(provider_name="Baltic Restaurants Estonia AS",
                                  canteens=[Canteen(name="Main building Deli cafe",
                                                    location="Ehitajate tee 5 U01 building",
                                                    time_open="2023-01-01 09:00",
                                                    time_closed="2023-01-01 16:30"),
                                            Canteen(name="Main building Daily lunch restaurant",
                                                    location="Ehitajate tee 5 U01 building",
                                                    time_open="2023-01-01 09:00",
                                                    time_closed="2023-01-01 16:30"),
                                            Canteen(name="Natural Science building canteen",
                                                    location="Akadeemia tee 15 SCI building",
                                                    time_open="2023-01-01 09:00",
                                                    time_closed="2023-01-01 16:00"),
                                            Canteen(name="ICT building canteen",
                                                    location="Raja 15/Mäepealse 1",
                                                    time_open="2023-01-01 09:00",
                                                    time_closed="2023-01-01 16:00")]),
                         Provider(provider_name="TTÜ Sport OÜ",
                                  canteens=[Canteen(name="Sports building canteen",
                                                    location="Männiliiva 7 S01 building",
                                                    time_open="2023-01-01 11:00",
                                                    time_closed="2023-01-01 20:00")])])
        session.commit()

    except:
        session.rollback()


def get_canteens_open_between_four_fifteen_and_six():
    """Return all canteens from db which are open 16.15-18.00"""
    try:
        rows = session.query(Canteen).filter(Canteen.time_open <= "2023-01-01 16:15",
                                             Canteen.time_closed >= "2023-01-01 18:00")
        for row in rows:
            print(row.name + ", " + row.location)
    except:
        session.rollback()
        raise


def get_canteens_serviced_by_rahva_toit():
    """Return all canteens which are serviced by Rahva Toit service provider."""
    try:
        rows = session.query(Canteen) \
            .join(Provider, Canteen.provider_id == Provider.id).filter(Provider.provider_name == "Rahva Toit")
        for row in rows:
            print(row.name)
    except:
        session.rollback()
        raise


# Executing all the functions
# create_tables()
# add_it_college()
# add_other_providers_and_canteens()
# get_canteens_open_between_four_fifteen_and_six()
# get_canteens_serviced_by_rahva_toit()

# close the connection
engine.dispose()
