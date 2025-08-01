**🛸 外星人入侵（Alien Invasion）**

一个基于 Python + Pygame 的经典射击游戏，你将驾驶飞船消灭入侵的外星舰队，随着关卡提升，游戏难度逐步升级。

**📁 项目结构**

    alien_invasion/
    ├── alien.py              # 外星人类
    ├── bullet.py             # 子弹类
    ├── button.py             # 按钮类（用于开始游戏）
    ├── game_stats.py         # 游戏状态管理
    ├── scoreboard.py         # 记分牌管理
    ├── settings.py           # 游戏设置
    ├── ship.py               # 飞船类
    ├── alien_invasion.py     # 游戏主入口
    ├── images/               # 存放图片资源（如飞船、外星人）
    └── README.md             # 项目说明文档

**🕹️ 游戏玩法**

- 点击 Play 按钮或者按 P 键可开始游戏
- 使用 → / ← 控制飞船左右移动
- 使用 空格 键发射子弹
- 消灭所有外星人以进入下一关
- 飞船生命用完后，游戏结束
- 按 Q 键可退出游戏

**🔧 安装和运行**

1.安装 Python 和 Pygame

确保你已安装 Python 3.x（推荐 3.10+）,然后安装 Pygame：

    python --version

    pip install pygame

2.运行游戏
    
	python alien_invasion.py

**⚙️ 自定义内容**

你可以通过修改以下设置进行游戏调优：

- 难度提升速度：settings.py 中 speedup_scale

- 飞船生命限制：settings.py 中 ship_limit

- 子弹数量上限：settings.py 中 bullets_allowed

- 飞船 / 外星人图像：替换 images/ 文件夹中的 .bmp 图像

**🧠 学习资源推荐**

本项目适合学习以下内容：

- Python 类和模块结构

- Pygame 游戏循环与事件处理

- 碰撞检测、动画与渲染

- 状态管理与界面更新

该游戏原型基于 《Python编程：从入门到实践》 中的项目设计。

**📌 TODO 可扩展功能**

- 加入音效和背景音乐

- 增加敌人类型（如 Boss 外星人）

- 排行榜保存功能

- 多人合作模式

- 移动端支持

**📄 许可证（License）**

本项目仅用于学习交流目的，版权归原作者所有。
