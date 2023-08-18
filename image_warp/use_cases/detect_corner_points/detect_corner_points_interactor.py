from typing import cast

from ...domain.models.image import Image
from ...domain.models.image_bytes import ImageBytes
from ...domain.models.image_extension import ImageExtension
from .._abc import ABCInputData, ABCInteractor, ABCOutputData
from .._commons.coordinate_point import CoordinatePoint
from .._commons.corner_points import CornerPoints
from .detect_corner_points_input_data import DetectCornerPointsInputData
from .detect_corner_points_output_data import DetectCornerPointsOutputData


class DetectCornerPointsInteractor(ABCInteractor):
    def handle(self, input_data: ABCInputData) -> ABCOutputData:
        input_data = cast(DetectCornerPointsInputData, input_data)

        image_bytes = ImageBytes(value=input_data.image_bytes)
        image_extension = ImageExtension(value=input_data.image_extension)

        image_processor = Image(
            image_bytes=image_bytes, image_extension=image_extension
        )
        detected_points = image_processor.detect_corner_points()

        if detected_points is None:
            return DetectCornerPointsOutputData(corner_points=None)

        return DetectCornerPointsOutputData(
            corner_points=CornerPoints(
                top_left=CoordinatePoint(
                    x=detected_points.top_left.value_x,
                    y=detected_points.top_left.value_y,
                ),
                top_right=CoordinatePoint(
                    x=detected_points.top_right.value_x,
                    y=detected_points.top_right.value_y,
                ),
                bottom_right=CoordinatePoint(
                    x=detected_points.bottom_right.value_x,
                    y=detected_points.bottom_right.value_y,
                ),
                bottom_left=CoordinatePoint(
                    x=detected_points.bottom_left.value_x,
                    y=detected_points.bottom_left.value_y,
                ),
            )
        )
