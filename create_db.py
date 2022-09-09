# This script should be ran first.
from db import Base, engine, SessionLocal
from models import Announcement

Base.metadata.create_all(engine)
