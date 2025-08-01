import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # 加载飞船图像并获取其 rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 初始位置：屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 使用浮点数存储精确位置
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 更新 rect 对象的位置
        self.rect.x = self.x

    def draw_ship(self):
        """在屏幕上绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船放回屏幕底部中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
