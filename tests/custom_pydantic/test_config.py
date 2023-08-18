import pytest
from pydantic import BaseModel, ValidationError

from custom_pydantic.config import BaseConfigDict, BaseFrozenConfigDict


class TestBaseConfigDict:
    class Model(BaseModel):
        model_config = BaseConfigDict

        prop_int: int

    class InvalidModel(BaseModel):
        model_config = BaseConfigDict

        prop_int: int = "1"  # type: ignore[assignment]

    def test_strict_true(self) -> None:
        with pytest.raises(ValidationError):
            self.Model(prop_int="1")  # type: ignore[arg-type]

    def test_validate_default_true(self) -> None:
        with pytest.raises(ValidationError):
            self.InvalidModel()

    def test_extra_forbid(self) -> None:
        with pytest.raises(ValidationError):
            self.Model(prop_int=1, add_prop="test")  # type: ignore[call-arg]


class TestBaseFrozenConfigDict:
    class Model(BaseModel):
        model_config = BaseFrozenConfigDict

        prop_int: int

    def test_frozen_true(self) -> None:
        model = self.Model(prop_int=1)

        with pytest.raises(ValidationError):
            model.prop_int = 2
