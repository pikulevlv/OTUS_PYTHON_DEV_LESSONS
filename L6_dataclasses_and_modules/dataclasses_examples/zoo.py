# class Zoo:
#
#     def __init__(self, animals):
#         self.animals= animals

from dataclasses import dataclass, field
from typing import List
from animals import Bear

@dataclass
class Zoo:
    animals: List[Bear] = field(default_factory=list) # такое дефолтное значения устанавливает по умолчанию список (да, непривычно)