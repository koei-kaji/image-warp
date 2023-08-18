from typing import Tuple, cast

from image_warp.use_cases._commons.coordinate_point import CoordinatePoint
from image_warp.use_cases._commons.corner_points import CornerPoints
from image_warp.use_cases.warp_transform import (
    WarpTransformInputData,
    WarpTransformInteractor,
    WarpTransformOutputData,
)


def test_normal(fixt_image_form: Tuple[bytes, str]) -> None:
    bytes, ext = fixt_image_form
    converted_points = CornerPoints(
        top_left=CoordinatePoint(x=29, y=228),
        top_right=CoordinatePoint(x=571, y=150),
        bottom_right=CoordinatePoint(x=728, y=861),
        bottom_left=CoordinatePoint(x=131, y=986),
    )

    input_data = WarpTransformInputData(
        image_bytes=bytes,
        image_extension=ext,  # type: ignore[arg-type]
        converted_points=converted_points,
    )
    interactor = WarpTransformInteractor()
    output_data = cast(WarpTransformOutputData, interactor.handle(input_data))

    assert output_data is not None
