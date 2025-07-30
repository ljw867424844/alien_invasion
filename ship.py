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
        # 在飞船的属性x中存储一个浮点数
        self.x = float(self.rect.x)
        # 移动标志（飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据据self.x更新rect对象
        self.rect.x = self.x
        
    def draw(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
