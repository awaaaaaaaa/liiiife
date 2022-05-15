import pygame
from color import color

class button:
    def __init__(self, title, pos, size, bg_color, text_color, font_size=30):
        self.title = title
        self.pos = pos
        self.size = size
        self.bg_color = bg_color
        self.text_color = text_color
        self.font_size = font_size
        self.old_color = bg_color

    def draw(self, window):
        pygame.draw.rect(window, self.bg_color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        DefaultFont = pygame.font.get_default_font()
        font = pygame.font.Font(DefaultFont, self.font_size)
        text = font.render(self.title, True, self.text_color)
        t_w, t_h = text.get_size()
        window.blit(text, (self.pos[0] + self.size[0] / 2 - t_w / 2, self.pos[1] + self.size[1] / 2 - t_h / 2))

    def is_down(self, pos, window):
        m_x, m_y, = pos
        btn_x, btn_y = self.pos
        btn_w, btn_h = self.size
        if btn_x <= m_x <= btn_x + btn_w and btn_y <= m_y <= btn_y + btn_h:
            self.bg_color = color.orange
            self.draw(window)
            pygame.display.update()
            return True

        return False

    def btn_up(self, window):
        self.bg_color = color.blue
        self.draw(window)
        pygame.display.update()
