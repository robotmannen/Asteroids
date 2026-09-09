import pygame


class ScoreBoard:
    containers: tuple[pygame.sprite.Group, ...]
    score = 0
    score_text = "Score: 0"

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("arial", 96)

    def draw(self):
        return self.font.render(self.score_text, True, (255, 255, 255))

    def get_size(self):
        return self.font.size(self.score_text)

    def add_score(self):
        self.score += 1
        self.score_text = f"Score: {self.score}"
