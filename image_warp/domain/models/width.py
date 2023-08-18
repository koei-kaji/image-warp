from pydantic import NonNegativeInt

from ._base_model import ValueObjectModel


class Width(ValueObjectModel):
    value: NonNegativeInt
