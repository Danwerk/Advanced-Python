"""
Development environment
Windows 10
IDE Pycharm
python3 version: 3.6

Author: Danyil Kurbatov
"""
import sqlite3


class Db:
    """Class Db. This contains all sql queries, db connection, tables creation and records creation methods."""

    def __init__(self):
        """Db constructor. initialize database path and DB name."""
        self.path = '../database/DINERS.db'

    def opendb(self):
        """Establish sqlite connection - open SQLite database.
        path is used as  connection variable."""
        conn = sqlite3.connect(self.path)
        print("DB connection established successfully")
        return conn

    def create_canteen_table(self):
        """Create a CANTEEN table in database."""
        conn = self.opendb()
        conn.execute('''CREATE TABLE CANTEEN
                     (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
                     NAME           TEXT    NOT NULL,
                     LOCATION       TEXT     NOT NULL,
                     TIME_OPEN      TEXT,
                     TIME_CLOSED    TEXT, 
                     PROVIDER_ID    INTEGER,
                     FOREIGN KEY (PROVIDER_ID) REFERENCES PROVIDER(PROVIDER_ID));''')
        conn.commit()
        conn.close()

    def create_provider_table(self):
        """Create a PROVIDER table in database."""
        conn = self.opendb()
        conn.execute('''CREATE TABLE PROVIDER
                     (PROVIDER_ID INTEGER PRIMARY KEY     AUTOINCREMENT,
                     PROVIDER_NAME           TEXT    NOT NULL)''')
        conn.commit()
        conn.close()

    def create_records(self):
        conn = self.opendb()

        # IT College canteen and provider data as separate statement
        itcollege_provider = 'insert into PROVIDER (PROVIDER_ID, PROVIDER_NAME) values (4, "bitStop")'
        conn.execute(itcollege_provider)

        itcollege_canteen = 'insert into CANTEEN (NAME, LOCATION, TIME_OPEN, TIME_CLOSED, PROVIDER_ID) values ' \
                            '("bitStop KOHVIK","Raja 4C","2023-01-01 09:30","2023-01-01 16:00", 4)'
        conn.execute(itcollege_canteen)

        # Other University canteens and providers data
        providers = 'insert into PROVIDER (PROVIDER_ID, PROVIDER_NAME) values (1, "Rahva Toit"),' \
                    '(2, "Baltic Restaurants Estonia AS"),(3, "TTÜ Sport OÜ")'
        conn.execute(providers)

        canteens = 'insert into CANTEEN (NAME, LOCATION, TIME_OPEN, TIME_CLOSED, PROVIDER_ID) values ' \
                   '("Economics- and social science building canteen","Akadeemia tee 3 SOC- building","2023-01-01 08:30","2023-01-01 18:30", 1),' \
                   '("Libary canteen","Akadeemia tee 1/Ehitajate tee 7","2023-01-01 08:30","2023-01-01 19:00", 1), ' \
                   '("Main building Deli cafe","Ehitajate tee 5 U01 building","2023-01-01 09:00","2023-01-01 16:30", 2), ' \
                   '("Main building Daily lunch restaurant","Ehitajate tee 5 U01 building","2023-01-01 09:00","2023-01-01 16:30", 2), ' \
                   '("U06 building canteen","","2023-01-01 09:00","2023-01-01 16:00", 1),' \
                   '("Natural Science building canteen","Akadeemia tee 15 SCI building","2023-01-01 09:00","2023-01-01 16:00", 2),' \
                   '("ICT building canteen","Raja 15/Mäepealse 1","2023-01-01 09:00","2023-01-01 16:00", 2), ' \
                   '("Sports building canteen","Männiliiva 7 S01 building","2023-01-01 11:00","2023-01-01 20:00", 3)'
        conn.execute(canteens)

        conn.commit()
        conn.close()

    def get_canteens_open_between_four_fifteen_and_six(self):
        """Return all canteens from db which are open 16.15-18.00"""
        conn = self.opendb()
        rows = conn.execute(
            'select NAME, LOCATION from CANTEEN where TIME_OPEN <= "2023-01-01 16:15" and TIME_CLOSED >= "2023-01-01 18:00"')
        for row in rows:
            print(row[0] + ", " + row[1])

        conn.close()

    def get_canteens_serviced_by_rahva_toit(self):
        """Return all canteens which are serviced by Rahva Toit service provider."""
        conn = self.opendb()
        rows = conn.execute(
            'select CANTEEN.NAME from CANTEEN inner join PROVIDER on PROVIDER.PROVIDER_ID=CANTEEN.PROVIDER_ID where PROVIDER.PROVIDER_NAME="Rahva Toit"')
        for row in rows:
            print(row[0])
        conn.close()


if __name__ == '__main__':
    # create db instance, and database DINERS with it.
    db = Db()

    # create table CANTEEN
    # db.create_canteen_table()

    # create table PROVIDER
    # db.create_provider_table()

    # create records in the PROVIDER and CANTEEN tables
    # db.create_records()

    # Get canteens which are open 16.15-18.00
    # db.get_canteens_open_between_four_fifteen_and_six()

    # Get canteens which are serviced by Rahva Toit
    # db.get_canteens_serviced_by_rahva_toit()
