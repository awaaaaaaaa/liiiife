import pygame
from color import color

class cell:
    def __init__(self, pos, size, state):
        self.pos = pos
        self.size = size
        self.state = state

    def draw(self, new_color, window):
        m_x, m_y = self.pos
        btn_w, btn_h = self.size
        pygame.draw.rect(window, new_color, (m_x, m_y, btn_w, btn_h))

    def is_cell(self, pos, window):
        m_x, m_y, = pos
        btn_x, btn_y = self.pos
        btn_w, btn_h = self.size
        if btn_x <= m_x <= btn_x + btn_w and btn_y <= m_y <= btn_y + btn_h:
            new_color = color.black
            if self.state == 1:
                new_color = color.white
            self.draw(new_color, window)
            pygame.display.update()
            return True

        return False
