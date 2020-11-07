from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean
# import sqlite3

engine = create_engine("sqlite:///example.db") # can create the file anywhere
metadata = MetaData()

#create simple table
users_table = Table("users",
                    metadata,
                    Column("id", Integer, primary_key=True), # set name of col, type, primary key or not
                    Column("username", String(32), unique=True),
                    Column("is_staff", Boolean, default=False),
                    )

if __name__ == '__main__':
    # metadata know about all tabs we registered, uses engine for connecting to DB ("sqlite:///example.db")
    metadata.create_all(engine) # example.db created