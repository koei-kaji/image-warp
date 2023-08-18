from pydantic import NonNegativeInt

from ._base_model import ValueObjectModel


class CoordinatePoint(ValueObjectModel):
    value_x: NonNegativeInt
    value_y: NonNegativeInt
