from enum import IntEnum
class ConnectionType(IntEnum):
  NoConnection = 0
  Or = 1
  And = 2

  def __str__(self) -> str:
    strings = ["", "or", "and"]
    return strings[self]