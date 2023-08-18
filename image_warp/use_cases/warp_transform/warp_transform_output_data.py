from typing import Literal

from .._abc import ABCOutputData


class WarpTransformOutputData(ABCOutputData):
    image_bytes: bytes
    image_extension: Literal["jpg", "png"]
