import abc

from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfigDict


class ABCInputData(BaseModel, abc.ABC):
    model_config = BaseFrozenConfigDict
