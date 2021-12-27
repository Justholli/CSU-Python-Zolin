from sqlalchemy.orm import Session

from . import models, schemas


def create_manufacturer(db: Session, manufacturer: schemas.ManufacturerCreate):
    db_manufacturer = models.Manufacturer(
        prName=manufacturer.prname,
        country=manufacturer.country
    )
    db.add(db_manufacturer)
    db.commit()
    db.refresh(db_manufacturer)
    return db_manufacturer


def create_good(db: Session, good: schemas.GoodCreate, manufacturerId: int):
    db_good = models.Good(name=good.name,
                          manufacturerId=manufacturerId,
                          price=good.price
                          )
    db.add(db_good)
    db.commit()
    db.refresh(db_good)
    return db_good


def create_storage(db: Session, storage: schemas.StorageCreate, good_id):
    db_storage = models.Storage(
        goodId=good_id,
        count=storage.count
    )
    db.add(db_storage)
    db.commit()
    db.refresh(db_storage)
    return db_storage


def create_size(db: Session, size: schemas.SizeCreate, good_id):
    db_size = models.Storage(
        goodId=good_id,
        size=size.size
    )
    db.add(db_size)
    db.commit()
    db.refresh(db_size)
    return db_size
