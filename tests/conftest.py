from pathlib import Path
from typing import Tuple

import cv2
import pytest

base_path = Path(__file__).resolve().parent


def _image_bytes(path: Path) -> bytes:
    image = cv2.imread(str(path))
    _, buffer = cv2.imencode(path.suffix, image)

    return buffer.tobytes()


@pytest.fixture(scope="session")
def fixt_path_lenna() -> Path:
    return base_path / "img/lenna.png"


@pytest.fixture(scope="session")
def fixt_path_form() -> Path:
    return base_path / "img/form.jpg"


@pytest.fixture(scope="session")
def fixt_image_lenna(fixt_path_lenna: Path) -> Tuple[bytes, str]:
    return _image_bytes(fixt_path_lenna), fixt_path_lenna.suffix.lstrip(".")


@pytest.fixture(scope="session")
def fixt_image_form(fixt_path_form: Path) -> bytes:
    return _image_bytes(fixt_path_form), fixt_path_form.suffix.lstrip(".")
