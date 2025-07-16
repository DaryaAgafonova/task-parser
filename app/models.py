from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

problem_tags = Table(
    "problem_tags",
    Base.metadata,
    Column("problem_id", Integer, ForeignKey("problems.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True)
    contest_id = Column(Integer)
    index = Column(String)
    name = Column(String)
    rating = Column(Integer)
    solved_count = Column(Integer)
    tags = relationship("Tag", secondary=problem_tags, back_populates="problems")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    problems = relationship("Problem", secondary=problem_tags, back_populates="tags")
