from typing import Literal

from ._base_model import ValueObjectModel


class ImageExtension(ValueObjectModel):
    value: Literal["jpg", "png"]
