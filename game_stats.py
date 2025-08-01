class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏期间不会重置的统计信息
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit - 1
        self.score = 0
        self.level = 1
