from __future__ import annotations

import cv2
import numpy as np

from ._base_model import ValueObjectModel
from .image_extension import ImageExtension


class ImageBytes(ValueObjectModel):
    value: bytes

    def decode(self) -> np.ndarray:  # type: ignore[type-arg]
        image_array = np.frombuffer(self.value, np.uint8)
        return cv2.imdecode(image_array, cv2.IMREAD_COLOR)  # type: ignore[no-any-return]

    @staticmethod
    def encode(image: np.ndarray, extension: ImageExtension) -> ImageBytes:  # type: ignore[type-arg]
        _, buffer = cv2.imencode(f".{extension.value}", image)
        return ImageBytes(value=buffer.tobytes())
