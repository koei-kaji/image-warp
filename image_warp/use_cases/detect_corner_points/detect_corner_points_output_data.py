from .._abc import ABCOutputData
from .._commons.corner_points import CornerPoints


class DetectCornerPointsOutputData(ABCOutputData):
    corner_points: CornerPoints | None
