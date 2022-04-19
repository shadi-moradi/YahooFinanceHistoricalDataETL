from dataclasses import dataclass

@dataclass
class SqlStatusResult:
    isSuccess: bool = None
    description: str = None
    data: list = None

