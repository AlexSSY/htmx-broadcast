from faker import Faker
from sqlalchemy import asc, desc

from models import Foo
from db import SessionLocal


def foo_list(offset = 0, limit = 100, sort=('id', 'asc')) -> list[Foo]:
    with SessionLocal() as db:
        query = db.query(Foo)
        
        if sort[0] in Foo.__table__.columns:
            column = getattr(Foo, sort[0])
            query = query.order_by(desc(column) if sort[1] == "desc" else asc(column))
        
        return query.offset(offset).limit(limit)


faker = Faker()
def foo_add_random() -> Foo | None:
    with SessionLocal() as db:
        new_instance = Foo(name=faker.name(), description=faker.company())
        db.add(new_instance)
        db.commit()
        db.refresh(new_instance)
        return new_instance


def foo_delete(id) -> Foo | None:
    with SessionLocal() as db:
        # db.query(Foo).where(Foo.id == id).delete(synchronize_session=False)
        instance = db.get(Foo, id)
        db.delete(instance)
        db.commit()
        return instance


def foo_update(id, name, description) -> Foo | None:
    with SessionLocal() as db:
        foo = db.get(Foo, id)
        foo.name = name
        foo.description = description
        db.commit()
        db.refresh(foo)
        return foo
