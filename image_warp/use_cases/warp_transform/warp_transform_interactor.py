from typing import cast

from ...domain.models.coordinate_point import CoordinatePoint
from ...domain.models.corner_points import CornerPoints
from ...domain.models.image import Image
from ...domain.models.image_bytes import ImageBytes
from ...domain.models.image_extension import ImageExtension
from .._abc import ABCInputData, ABCInteractor, ABCOutputData
from .warp_transform_input_data import WarpTransformInputData
from .warp_transform_output_data import WarpTransformOutputData


class WarpTransformInteractor(ABCInteractor):
    def handle(self, input_data: ABCInputData) -> ABCOutputData:
        input_data = cast(WarpTransformInputData, input_data)

        image_bytes = ImageBytes(value=input_data.image_bytes)
        image_extension = ImageExtension(value=input_data.image_extension)

        corner_points = CornerPoints(
            top_left=CoordinatePoint(
                value_x=input_data.converted_points.top_left.x,
                value_y=input_data.converted_points.top_left.y,
            ),
            top_right=CoordinatePoint(
                value_x=input_data.converted_points.top_right.x,
                value_y=input_data.converted_points.top_right.y,
            ),
            bottom_right=CoordinatePoint(
                value_x=input_data.converted_points.bottom_right.x,
                value_y=input_data.converted_points.bottom_right.y,
            ),
            bottom_left=CoordinatePoint(
                value_x=input_data.converted_points.bottom_left.x,
                value_y=input_data.converted_points.bottom_left.y,
            ),
        )

        image = Image(image_bytes=image_bytes, image_extension=image_extension)
        warped_image_data = image.warp_transform(
            input_points=corner_points,
        )

        return WarpTransformOutputData(
            image_bytes=warped_image_data.value,
            image_extension=image_extension.value,
        )
