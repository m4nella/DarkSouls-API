# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy.orm import Session
# from typing import List, Optional
# import models
# from database import engine, SessionLocal

# app = FastAPI()

# models.Base.metadata.create_all(bind=engine)


# # Models
# class CharacterBase(BaseModel):
#     name: str
#     level: int
#     class_name: str
#     starting_gift: str
#     covenant: str


# class CharacterCreate(CharacterBase):
#     pass


# class ItemBase(BaseModel):
#     name: str
#     type: str
#     description: str
#     required_level: int
#     required_class: str


# class ItemCreate(ItemBase):
#     pass


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Routes
# @app.post("/characters/", response_model=models.Character)
# def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
#     db_character = models.Character(**character.dict())
#     db.add(db_character)
#     db.commit()
#     db.refresh(db_character)
#     return db_character


# @app.post("/items/", response_model=models.Item)
# def create_item(item: ItemCreate, db: Session = Depends(get_db)):
#     db_item = models.Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


# @app.get("/characters/{character_id}", response_model=models.Character)
# def read_character(character_id: int, db: Session = Depends(get_db)):
#     return db.query(models.Character).filter(models.Character.id == character_id).first()


# @app.get("/items/{item_id}", response_model=models.Item)
# def read_item(item_id: int, db: Session = Depends(get_db)):
#     return db.query(models.Item).filter(models.Item.id == item_id).first()


# @app.get("/characters/", response_model=List[models.Character])
# def read_characters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return db.query(models.Character).offset(skip).limit(limit).all()


# @app.get("/items/", response_model=List[models.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
