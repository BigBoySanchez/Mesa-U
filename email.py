import pygame
import game_config

# solution is the name of the object that was pressed
# ex: delete, reply, link (sent from subject)
class email:
    def __init__(self, subject, name, address, body, solution):
        self.subject = subject
        self.name = name
        self.address = address
        self.body = body
        self.solution = solution

    def check_solution(self, name):
        return name == self.solution

    