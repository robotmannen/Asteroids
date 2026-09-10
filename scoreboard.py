import pygame
from constants import SCREEN_WIDTH


class ScoreBoard:
    containers: tuple[pygame.sprite.Group, ...]
    score = 0
    score_text = "Score: 0"

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("arial", 96)

    def draw(self):
        return self.font.render(self.score_text, True, (255, 255, 255))

    def get_position(self):
        return ((SCREEN_WIDTH / 2) - self.font.size(self.score_text)[0] / 2)

    def add_score(self):
        self.score += 1
        self.score_text = f"Score: {self.score}"
