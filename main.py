from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class CharacterBase(BaseModel):
    name: str
    level: int
    class_name: str
    starting_gift: str
    covenant: str


class ItemBase(BaseModel):
    name: str
    type: str
    description: str
    required_level: int
    required_class: str


class ItemCreate(ItemBase):
    pass


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemBase, db: db_dependency):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()


@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: int, db: db_dependency):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        HTTPException(status_code=404, detail='Item not found')
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_200_OK)
async def delete_item(item_id: int, db: db_dependency):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail='Item was not found')
    db.delete(db_item)
    db.commit()


@app.post("/characters/", status_code=status.HTTP_201_CREATED)
async def create_character(character: CharacterBase, db: db_dependency):
    db_character = models.Character(**character.dict())
    db.add(db_character)
    db.commit()


@app.get("/characters/{character_id}", status_code=status.HTTP_200_OK)
async def read_character(character_id: int, db: db_dependency):
    character = db.query(models.Character).filter(models.Character.id == character_id).first()
    if character is None:
        raise HTTPException(status_code=404, detail='Character not found')
    return character