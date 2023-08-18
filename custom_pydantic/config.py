from pydantic import ConfigDict

BaseConfigDict = ConfigDict(
    strict=True,
    validate_default=True,
    extra="forbid",
)

BaseFrozenConfigDict = ConfigDict(
    **BaseConfigDict,
    frozen=True,
)
