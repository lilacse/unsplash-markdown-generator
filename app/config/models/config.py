from dataclasses import dataclass


@dataclass
class Config:
    token: str = ""
    template: str = ""
