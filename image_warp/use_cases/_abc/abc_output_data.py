import abc

from pydantic import BaseModel

from custom_pydantic.config import BaseFrozenConfigDict


class ABCOutputData(BaseModel, abc.ABC):
    model_config = BaseFrozenConfigDict
