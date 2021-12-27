from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/manufacturer/", response_model=schemas.Manufacturer)
def create_manufacturer(manufacturer: schemas.ManufacturerCreate, db: Session = Depends(get_db)):
    return crud.create_manufacturer(db=db, manufacturer=manufacturer)


@app.post("/storage/", response_model=schemas.Storage)
def create_storage(storage: schemas.StorageCreate, db: Session = Depends(get_db)):
    return crud.create_storage(db=db, storage=storage)


@app.post("/storage/goods/", response_model=schemas.Good)
def add_good_for_storage(
        good: schemas.GoodCreate, manufacturer: schemas.Manufacturer, db: Session = Depends(get_db)
):
    return crud.create_good(db=db, good=good, manufacturerId=manufacturer.manufacturerId)
