import numpy as np

from image_warp.domain.models.coordinate_point import CoordinatePoint
from image_warp.domain.models.corner_points import CornerPoints
from image_warp.domain.models.height import Height
from image_warp.domain.models.width import Width


class TestConvertNpFloat32:
    def test_normal(self) -> None:
        described_class = CornerPoints(
            top_left=CoordinatePoint(value_x=10, value_y=20),
            top_right=CoordinatePoint(value_x=30, value_y=40),
            bottom_right=CoordinatePoint(value_x=50, value_y=60),
            bottom_left=CoordinatePoint(value_x=70, value_y=80),
        )
        result = described_class.convert_np_float32()
        expected = np.float32([[10, 20], [30, 40], [50, 60], [70, 80]])  # type: ignore[arg-type]

        assert np.array_equal(result, expected)


class TestCalculateNormalizedPoints:
    def test_normal(self) -> None:
        described_class = CornerPoints(
            top_left=CoordinatePoint(value_x=10, value_y=20),
            top_right=CoordinatePoint(value_x=30, value_y=40),
            bottom_right=CoordinatePoint(value_x=50, value_y=60),
            bottom_left=CoordinatePoint(value_x=70, value_y=80),
        )
        (
            result_points,
            result_width,
            result_height,
        ) = described_class.calculate_normalized_points()
        expected_points = CornerPoints(
            top_left=CoordinatePoint(value_x=0, value_y=0),
            top_right=CoordinatePoint(value_x=28, value_y=0),
            bottom_right=CoordinatePoint(value_x=28, value_y=84),
            bottom_left=CoordinatePoint(value_x=0, value_y=84),
        )
        expected_result_width = Width(value=28)
        expected_result_height = Height(value=84)

        assert result_points == expected_points
        assert result_width == expected_result_width
        assert result_height == expected_result_height
