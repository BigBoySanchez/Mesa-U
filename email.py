import pygame
import game_config

# solution is the name of the object that was pressed
# ex: delete, reply, link (sent from subject)
class Email:
    def __init__(self, subject, name, address, body, solution, why):
        self.subject = subject
        self.name = name
        self.address = address
        self.body = body            # surface
        self.solution = solution
        self.why = why

    def check_solution(self, name):
        return name == self.solution



