from sqlalchemy import (Table, Column, Float, Date, String, Text, Integer)

from db import Base


class Announcement(Base):
    __tablename__ = 'announcements'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    location = Column(String(64))
    date = Column(Date)
    price = Column(Float)
    currency = Column(String(3))
    beds = Column(String(32))
    description = Column(Text)
    image_url = Column(String(255))

    def __repr__(self):
        return f"<Announcement title={self.title[:25]}... price={self.price}>"
