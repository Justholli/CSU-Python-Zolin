from typing import List, Optional

from pydantic import BaseModel


class GoodBase(BaseModel):
    name: str
    price: float


class GoodCreate(GoodBase):
    pass


class Good(GoodBase):
    goodId: int
    manufacturerId: int

    class Config:
        orm_mode = True


class StorageBase(BaseModel):
    count: int


class StorageCreate(StorageBase):
    pass


class Storage(StorageBase):
    id: int
    goods: List[Good] = []

    class Config:
        orm_mode = True


class ManufacturerBase(BaseModel):
    prName: str
    country: str


class ManufacturerCreate(ManufacturerBase):
    pass


class Manufacturer(ManufacturerBase):
    manufacturerId: int

    class Config:
        orm_mode = True


class SizeBase(BaseModel):
    size: float


class SizeCreate(SizeBase):
    pass


class Size(SizeBase):
    id: int

    class Config:
        orm_mode = True
