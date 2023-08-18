from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfigDict


class CoordinatePoint(BaseModel):
    model_config = BaseFrozenConfigDict

    x: int
    y: int
