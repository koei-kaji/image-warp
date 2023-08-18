from typing import Tuple

from image_warp.domain.models.coordinate_point import CoordinatePoint
from image_warp.domain.models.corner_points import CornerPoints
from image_warp.domain.models.image import Image
from image_warp.domain.models.image_bytes import ImageBytes
from image_warp.domain.models.image_extension import ImageExtension


class TestDetectCornerPoints:
    def test_normal(self, fixt_image_form: Tuple[bytes, str]) -> None:
        bytes, ext = fixt_image_form
        described_class = Image(
            image_bytes=ImageBytes(value=bytes),
            image_extension=ImageExtension(value=ext),  # type: ignore[arg-type]
        )

        result = described_class.detect_corner_points()

        assert type(result) is CornerPoints

    def test_none(self, fixt_image_lenna: Tuple[bytes, str]) -> None:
        bytes, ext = fixt_image_lenna
        described_class = Image(
            image_bytes=ImageBytes(value=bytes),
            image_extension=ImageExtension(value=ext),  # type: ignore[arg-type]
        )

        result = described_class.detect_corner_points()

        assert result is None


class TestWarpTransform:
    def test_normal(self, fixt_image_form: Tuple[bytes, str]) -> None:
        bytes, ext = fixt_image_form
        described_class = Image(
            image_bytes=ImageBytes(value=bytes),
            image_extension=ImageExtension(value=ext),  # type: ignore[arg-type]
        )

        input_points = CornerPoints(
            top_left=CoordinatePoint(value_x=29, value_y=228),
            top_right=CoordinatePoint(value_x=571, value_y=150),
            bottom_right=CoordinatePoint(value_x=728, value_y=861),
            bottom_left=CoordinatePoint(value_x=131, value_y=986),
        )

        result = described_class.warp_transform(input_points)

        assert result
