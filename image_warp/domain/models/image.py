from __future__ import annotations

from typing import Sequence

import cv2
import numpy as np

from ._base_model import EntityModel
from .coordinate_point import CoordinatePoint
from .corner_points import CornerPoints
from .image_bytes import ImageBytes
from .image_extension import ImageExtension


class Image(EntityModel):
    image_bytes: ImageBytes
    image_extension: ImageExtension

    def detect_corner_points(self) -> CornerPoints | None:
        def _biggest_contour(contours: Sequence[np.ndarray]) -> np.ndarray:  # type: ignore[type-arg]
            biggest = np.array([])
            max_area = 0.0
            for i in contours:
                area = cv2.contourArea(i)
                if area > 1000:
                    peri = cv2.arcLength(i, True)
                    approx = cv2.approxPolyDP(i, 0.015 * peri, True)
                    if area > max_area and len(approx) == 4:
                        biggest = approx
                        max_area = area

            return biggest

        np_image = self.image_bytes.decode()

        # modify image
        np_grayscale_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)
        np_grayscale_image = cv2.bilateralFilter(np_grayscale_image, 20, 30, 30)
        np_edged_image = cv2.Canny(np_grayscale_image, 10, 20)

        # detect contour
        contours, _ = cv2.findContours(
            np_edged_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        biggest_contour = _biggest_contour(contours)

        if np.size(biggest_contour) == 0:
            return None

        # retrieve pixel value in the original image
        points = biggest_contour.reshape(4, 2)
        input_points = np.zeros((4, 2), dtype="float32")
        points_sum = points.sum(axis=1)
        input_points[0] = points[np.argmin(points_sum)]
        input_points[3] = points[np.argmax(points_sum)]

        points_diff = np.diff(points, axis=1)
        input_points[1] = points[np.argmin(points_diff)]
        input_points[2] = points[np.argmax(points_diff)]

        return CornerPoints(
            top_left=CoordinatePoint(
                value_x=int(input_points[0][0]), value_y=int(input_points[0][1])
            ),
            top_right=CoordinatePoint(
                value_x=int(input_points[1][0]), value_y=int(input_points[1][1])
            ),
            bottom_right=CoordinatePoint(
                value_x=int(input_points[3][0]), value_y=int(input_points[3][1])
            ),
            bottom_left=CoordinatePoint(
                value_x=int(input_points[2][0]), value_y=int(input_points[2][1])
            ),
        )

    def warp_transform(self, input_points: CornerPoints) -> ImageBytes:
        np_image = self.image_bytes.decode()

        np_input_points = input_points.convert_np_float32()
        normailized_points, width, height = input_points.calculate_normalized_points()
        np_output_points = normailized_points.convert_np_float32()

        matrix = cv2.getPerspectiveTransform(np_input_points, np_output_points)
        np_warped_image = cv2.warpPerspective(
            np_image, matrix, (width.value, height.value)
        )

        return ImageBytes.encode(np_warped_image, self.image_extension)
