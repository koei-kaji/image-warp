from pydantic import BaseModel, NonNegativeInt

from custom_pydantic.config import BaseFrozenConfigDict


class CoordinatePoint(BaseModel):
    model_config = BaseFrozenConfigDict

    x: NonNegativeInt
    y: NonNegativeInt
