from typing import Tuple, cast

from image_warp.use_cases._commons.corner_points import CornerPoints
from image_warp.use_cases.detect_corner_points import (
    DetectCornerPointsInputData,
    DetectCornerPointsInteractor,
    DetectCornerPointsOutputData,
)


def test_normal(fixt_image_form: Tuple[bytes, str]) -> None:
    bytes, ext = fixt_image_form

    input_data = DetectCornerPointsInputData(
        image_bytes=bytes,
        image_extension=ext,  # type: ignore[arg-type]
    )
    interactor = DetectCornerPointsInteractor()
    output_data = cast(DetectCornerPointsOutputData, interactor.handle(input_data))

    assert type(output_data.corner_points) is CornerPoints


def test_none(fixt_image_lenna: Tuple[bytes, str]) -> None:
    bytes, ext = fixt_image_lenna

    input_data = DetectCornerPointsInputData(
        image_bytes=bytes,
        image_extension=ext,  # type: ignore[arg-type]
    )
    interactor = DetectCornerPointsInteractor()
    output_data = cast(DetectCornerPointsOutputData, interactor.handle(input_data))

    assert output_data.corner_points is None
