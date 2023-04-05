from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    email: str
    password: str
    followers: List[str] = field(default_factory=list) 



