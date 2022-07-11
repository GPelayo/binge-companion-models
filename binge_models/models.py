from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Series(Base):
    __tablename__ = "series"

    series_id = Column(String, primary_key=True)
    name = Column(String)
    season_count = Column(Integer)
    thumbnail_url = Column(String)

    def __init__(self, series_id: str, name: str):
        self.series_id = series_id
        self.name = name
        self.season_count = -1
        self.thumbnail_url = None
        self.episodes = []
        self.series_wide_trivia = []


class Episode(Base):
    __tablename__ = "episode"

    episode_id = Column(String, primary_key=True)
    name = Column(String)
    season = Column(Integer)
    series_id = Column(String, ForeignKey('series.series_id'))

    def __init__(self, episode_id: str, name: str, season: int, series_id: str):
        self.episode_id = episode_id
        self.name = name
        self.season = season
        self.series_id = series_id


class Trivia(Base):
    __tablename__ = "trivia"

    trivia_id = Column(String, primary_key=True)
    episode_id = Column(String, ForeignKey('episode.episode_id'))
    series_id = Column(String, ForeignKey('series.series_id'))
    score = Column(Integer)
    score_denominator = Column(Integer)
    text = Column(String)

    def __init__(self, trivia_id: str, text: str, series_id: str, episode_id: str = None):
        self.trivia_id = trivia_id
        self.score = -1
        self.score_denominator = -1
        self.text = text
        self.series_id = series_id
        self.episode_id = episode_id


class TriviaTag(Base):
    __tablename__ = "trivia_tag"

    trivia_tag_id = Column(Integer, primary_key=True)
    trivia_id = Column(String, ForeignKey('trivia.trivia_id'))
    text = Column(String)

    def __init__(self, trivia_id: str, text: str):
        self.trivia_id = trivia_id
        self.text = text