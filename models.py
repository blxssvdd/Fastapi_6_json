from typing import Union, Optional

from pydantic import BaseModel, field_validator, Field


class SpellModel(BaseModel):
    index: int = Field(..., description="Індекс запису")
    spell: str = Field(..., description="Нове заклинання")
    use: Optional[str] = Field(None, description="Використання")
