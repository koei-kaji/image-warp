from typing import Literal

from .._abc import ABCInputData


class DetectCornerPointsInputData(ABCInputData):
    image_bytes: bytes
    image_extension: Literal["jpg", "png"]
