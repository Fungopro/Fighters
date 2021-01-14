from __future__ import annotations
from abc import ABC, abstractmethod


class state:

    def __init__(self, d):
        self.durability = d
