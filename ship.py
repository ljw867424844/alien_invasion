import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其起始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # 加载原始飞船图像
        original_image = pygame.image.load('images/ship.bmp')

        # 设定缩放比例（例如缩小到原图的 20%）
        scale_factor = 0.2
        width = int(original_image.get_width() * scale_factor)
        height = int(original_image.get_height() * scale_factor)

        # 缩放图像
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()

        # 将飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
