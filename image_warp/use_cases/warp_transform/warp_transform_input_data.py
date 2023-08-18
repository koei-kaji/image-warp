from typing import Literal

from .._abc import ABCInputData
from .._commons.corner_points import CornerPoints


class WarpTransformInputData(ABCInputData):
    image_bytes: bytes
    image_extension: Literal["jpg", "png"]
    converted_points: CornerPoints
