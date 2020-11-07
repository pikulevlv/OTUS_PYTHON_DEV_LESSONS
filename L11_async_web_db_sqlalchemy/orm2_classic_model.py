from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import mapper # connect tables and models
# import sqlite3

engine = create_engine("sqlite:///example.db") # can create the file anywhere
metadata = MetaData()

#create simple table
users_table = Table("users",
                    metadata,
                    Column("id", Integer, primary_key=True), # set name of col, type, primary key or not
                    Column("username", String(32), unique=True),
                    Column("is_staff", Boolean, default=False),
                    # Column("profile_pic_url", String, default='', nullable=False),
                    )

class User:
    def __init__(self, id, username: str, is_staff: bool):
        """

        :param id:
        :param username:
        :param is_staff:
        """
        self.id = id
        self.username = username
        self.is_staff = is_staff

mapper(User, users_table)

if __name__ == '__main__':
    # metadata know about all tabs we registered, uses engine for connecting to DB ("sqlite:///example.db")
    metadata.create_all(engine) # example.db created