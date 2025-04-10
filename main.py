from fastapi import FastAPI, HTTPException, status, Query, Path
from fastapi.responses import JSONResponse
import uvicorn

from data_actions import get_db, save_db
from models import SpellModel


app = FastAPI()


@app.get("/spells/")
async def get_spells():
    return get_db()


@app.get("/spells/{index}/")
async def get_spell(index: int):
    spell = next((spell for spell in get_db() if spell.get("index") == index), None)
    return spell


# @app.post("/spells/")
# async def add_spell(
#     index: int = Query(..., description="Номер по порядку", gt=71),
#     spell: str = Query(..., description="Нове заклинання"),
#     use: str = Query(..., description="Опис")
# ):
#     new_spell = dict(index=index, spell=spell, use=use)
#     db = get_db()
#     db.append(new_spell)
#     save_db(db)
#     return "Нове заклинання успішно додано!"


@app.post("/spells/", status_code=status.HTTP_201_CREATED)
async def add_spell(spell_model: SpellModel):
    db = get_db()
    db.append(spell_model.model_dump())
    save_db(db)
    return JSONResponse("Нове заклинання успішно додано!")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)

