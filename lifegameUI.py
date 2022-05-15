import pygame
from lifegameLogic import lifegameLogic
from button import button
from color import color
from cell import cell
class lifegameUI:
    def __init__(self, row, column):
        pygame.init()
        self.window = pygame.display.set_mode((540, 610))
        self.frame = lifegameLogic(row, column)
        self.Event = pygame.USEREVENT + 1
        self.btnName = ['start', 'pause', 'reset', 'rand']
        self.btnPos = [[15 + i * 130, 15] for i in range(4)]
        self.btnSize = [100, 30]
        self.isClick = -1
        self.startBtn = button(self.btnName[0], self.btnPos[0], self.btnSize, color.blue, color.white)
        self.pauseBtn = button(self.btnName[1], self.btnPos[1], self.btnSize, color.blue, color.white)
        self.resetBtn = button(self.btnName[2], self.btnPos[2], self.btnSize, color.blue, color.white)
        self.randBtn  = button(self.btnName[3], self.btnPos[3], self.btnSize, color.blue, color.white)
        pygame.time.set_timer(self.Event, 500)

        pygame.display.set_caption("lifegame")
        self.window.fill(color.grey)
        self.startBtn.draw(self.window)
        self.pauseBtn.draw(self.window)
        self.resetBtn.draw(self.window)
        self.randBtn.draw(self.window)

    def draw(self):
        for i in range(self.frame.Row):
            for j in range(self.frame.Column):
                if self.frame.mp[i][j] == 0:
                    pygame.draw.rect(self.window, color.white, (i * 18, 70 + j * 18, 15, 15))
                else:
                    pygame.draw.rect(self.window, color.black, (i * 18, 70 + j * 18, 15, 15))
        pygame.display.update()

    def start(self):
        self.frame.isStart = 1

    def pause(self):
        self.frame.isStart = 0

    def reset(self):
        self.frame.reset()
        self.draw()

    def rand(self):
        self.frame.rand()
        self.draw()

    def run(self):
        pygame.display.flip()
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.startBtn.is_down(event.pos, self.window):
                        self.start()
                        self.isClick = 0
                    if self.pauseBtn.is_down(event.pos, self.window):
                        self.pause()
                        self.isClick = 1
                    if self.resetBtn.is_down(event.pos, self.window):
                        self.reset()
                        self.isClick = 2
                    if self.randBtn.is_down(event.pos, self.window):
                        self.rand()
                        self.isClick = 3
                    if self.frame.isStart == 0:
                        for i in range(self.frame.Row):
                            for j in range(self.frame.Column):
                                cl = cell((i * 18, 70 + j * 18), (15, 15), self.frame.mp[i][j])
                                if cl.is_cell((x, y), self.window):
                                    self.frame.mp[i][j] = 1 - self.frame.mp[i][j]
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.isClick == 0:
                        self.startBtn.btn_up(self.window)
                    if self.isClick == 1:
                        self.pauseBtn.btn_up(self.window)
                    if self.isClick == 2:
                        self.resetBtn.btn_up(self.window)
                    if self.isClick == 3:
                        self.randBtn.btn_up(self.window)
                elif event.type == self.Event:
                    if self.frame.isStart == 1:
                        self.frame.play()
                        self.draw()
if __name__ == '__main__':
    lifegame = lifegameUI(30, 30)
    lifegame.rand()
    lifegame.run()