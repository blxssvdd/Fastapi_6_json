from typing import Union, Optional

from pydantic import BaseModel, field_validator, Field, EmailStr

class MyException(BaseException):
    pass

class SpellModel(BaseModel):
    index: int = Field(..., description="Індекс запису")#, gt=0, lt=100)
    spell: str = Field(..., description="Нове заклинання")
    use: Optional[str] = Field(None, description="Використання")


    @field_validator("index")
    def check_index(cls, index):
        if 0 < index < 100:
            return index
        raise ValueError("Індекс повинен бути у діапазоні від 0 до 100 ☹️")

    @field_validator("spell")
    def check_spell(cls, spell):
        if len(spell) > 3:
            return spell.upper()
        raise ValueError("Заклинання повинно бути довшим за 3 символи ☹️")

class SpellModelResponse(BaseModel):
    index: int = Field(..., description="Індекс запису")
    spell: str = Field(..., description="Нове заклинання")
    use: Optional[str] = Field(None, description="Використання")


class UserModel(BaseModel):
    first_name: str = Field(...)
    email: EmailStr = Field(...)

    @field_validator("first_name")
    def check_first_name(cls, first_name: str):
        if all([first_name.isalpha() and len(first_name) >= 2]):
            return first_name
        raise ValueError("Ім'я повинно мати мінімум 2 символи, лише літери ☹️")

    