from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfigDict

from .coordinate_point import CoordinatePoint


class CornerPoints(BaseModel):
    model_config = BaseFrozenConfigDict

    top_left: CoordinatePoint
    top_right: CoordinatePoint
    bottom_left: CoordinatePoint
    bottom_right: CoordinatePoint
