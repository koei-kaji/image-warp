from __future__ import annotations

from typing import Tuple

import numpy as np

from ._base_model import EntityModel
from .coordinate_point import CoordinatePoint
from .height import Height
from .width import Width


class CornerPoints(EntityModel):
    top_left: CoordinatePoint
    top_right: CoordinatePoint
    bottom_right: CoordinatePoint
    bottom_left: CoordinatePoint

    def convert_np_float32(self) -> np.ndarray:  # type: ignore[type-arg]
        return np.float32(  # type: ignore[return-value]
            [  # type: ignore[arg-type]
                [self.top_left.value_x, self.top_left.value_y],
                [self.top_right.value_x, self.top_right.value_y],
                [self.bottom_right.value_x, self.bottom_right.value_y],
                [self.bottom_left.value_x, self.bottom_left.value_y],
            ]
        )

    def calculate_normalized_points(self) -> Tuple[CornerPoints, Width, Height]:
        np_points = self.convert_np_float32()

        value_width = int(
            max(
                np.linalg.norm(np_points[0] - np_points[1]),
                np.linalg.norm(np_points[2] - np_points[3]),
            )
        )
        value_height = int(
            max(
                np.linalg.norm(np_points[0] - np_points[3]),
                np.linalg.norm(np_points[1] - np_points[2]),
            )
        )

        normalized_points = CornerPoints(
            top_left=CoordinatePoint(value_x=0, value_y=0),
            top_right=CoordinatePoint(value_x=value_width, value_y=0),
            bottom_left=CoordinatePoint(value_x=0, value_y=value_height),
            bottom_right=CoordinatePoint(value_x=value_width, value_y=value_height),
        )
        width = Width(value=value_width)
        height = Height(value=value_height)

        return normalized_points, width, height
