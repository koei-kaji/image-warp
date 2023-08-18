from pydantic import NonNegativeInt

from ._base_model import ValueObjectModel


class Height(ValueObjectModel):
    value: NonNegativeInt
