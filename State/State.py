from __future__ import annotations
from abc import ABC, abstractmethod


@abstractmethod
class State:
    def __init__(self, d):
        self.durability = d

    def get_state(self):
        return

    def __str__(self):
        return
