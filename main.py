from typing import List, Optional

from fastapi import FastAPI, HTTPException, status, Query, Path
from fastapi.responses import JSONResponse
import uvicorn

from data_actions import get_db, save_db
from models import SpellModel, SpellModelResponse, UserModel


app = FastAPI()


@app.get("/spells/", response_model=List[SpellModelResponse], status_code=status.HTTP_202_ACCEPTED)
async def get_spells():
    return get_db()


@app.get("/spells/{index}/", response_model=SpellModelResponse, status_code=status.HTTP_202_ACCEPTED)
async def get_spell(index: int):
    spell = next((spell for spell in get_db() if spell.get("index") == index), None)
    if not spell:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Заклинання з id {index} не знайдено. ☹️")
    return spell


@app.post("/spells/", status_code=status.HTTP_201_CREATED)
async def add_spell(spell_model: SpellModel):
    db = get_db()
    db.append(spell_model.model_dump())
    save_db(db)
    return JSONResponse("Нове заклинання успішно додано! 😎")



@app.post("/users/", status_code=status.HTTP_201_CREATED)
def add_user(user: UserModel):
    return JSONResponse("Користувача успішно додано! 😎")



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)

