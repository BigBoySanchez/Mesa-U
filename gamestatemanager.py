import pygame

class GameStateManager:
    def __init__(self, currentState) -> None:
        self.currentState = currentState
    def get_state(self) -> str:
        return self.currentState
    def set_state(self, currentState) -> None:
        self.currentState = currentState