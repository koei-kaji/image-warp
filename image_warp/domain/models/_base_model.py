from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfigDict


class ValueObjectModel(BaseModel):
    model_config = BaseFrozenConfigDict


class EntityModel(BaseModel):
    model_config = BaseFrozenConfigDict
