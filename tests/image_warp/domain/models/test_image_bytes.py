from pathlib import Path

import cv2

from image_warp.domain.models.image_bytes import ImageBytes
from image_warp.domain.models.image_extension import ImageExtension


class TestDecode:
    def test_normal(self, fixt_path_lenna: Path) -> None:
        image = cv2.imread(str(fixt_path_lenna))
        _, buffer = cv2.imencode(fixt_path_lenna.suffix, image)

        described_class = ImageBytes(value=buffer.tobytes())
        result = described_class.decode()

        assert result.shape == image.shape


class TestEncode:
    def test_normal(self, fixt_path_lenna: Path) -> None:
        image = cv2.imread(str(fixt_path_lenna))
        extension = ImageExtension(value=fixt_path_lenna.suffix.lstrip("."))  # type: ignore[arg-type]

        result = ImageBytes.encode(image, extension=extension)

        assert result.value is not None
