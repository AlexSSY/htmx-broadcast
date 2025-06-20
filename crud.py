from faker import Faker

from models import Foo
from db import SessionLocal


def foo_list(offset = 0, limit = 100) -> list[Foo]:
    with SessionLocal() as db:
        return db.query(Foo).offset(offset).limit(limit).all()


faker = Faker()
def foo_add_random() -> Foo | None:
    with SessionLocal() as db:
        new_instance = Foo(name=faker.name(), description=faker.company())
        db.add(new_instance)
        db.commit()
        db.refresh(new_instance)
        return new_instance
