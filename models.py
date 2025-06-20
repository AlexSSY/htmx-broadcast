from sqlalchemy import Column, String, Integer, func
from db import Base, engine, SessionLocal
import faker


class Foo(Base):
    __tablename__ = 'Foos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)


def create_all_tables():
    Base.metadata.create_all(engine)


def seed():
    fk = faker.Faker()
    RECORDS = 10
    with SessionLocal() as db:
        total_records = db.query(func.count(Foo.id)).scalar()
        if total_records < RECORDS:
            for i in range(RECORDS):
                data = {
                    'name': fk.name(),
                    'description': fk.company()
                }
                db.add(Foo(**data))
            db.commit()
