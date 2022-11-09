from sqlalchemy import Column, String, Integer, or_, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class PlayLists(Base):
    __tablename__ = 'playlists'
    playlistid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def dict(self):
        return{
            "id": self.playlistid,
            "name": self.name 
        }

class Genres(Base):
    __tablename__ = 'genres'
    GenreId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def dict(self):
        return{
            "id": self.GenreId,
            "name": self.name 
        }
# create engine
engine = create_engine(r'sqlite:///chinook.db')
# create session
Session = sessionmaker(bind=engine)
session = Session()
# select
# SELECT * FROM PLayLists;

# # delete
# items = session.query(PlayLists, Genres).filter(PlayLists.playlistid == Genres.GenreId,or_(PlayLists.name == "Music",  PlayLists.name == "TV Shows")).all()

# for item in items:
#     print(item.dict())

for c, i in session.query(PlayLists, Genres).filter(PlayLists.playlistid == Genres.GenreId,or_(PlayLists.name == "Music",  PlayLists.name == "TV Shows")).all():
   item = PlayLists(playlistid = c.playlistid, name = c.name)
   print(item.dict())

# create
