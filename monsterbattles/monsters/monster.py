class Monster(object):
    def __init__(self, name, base_type, secondary_type=None, level=1):
        self.name = name
        self.base_type = base_type
        self.secondary_type = secondary_type

        self.level = level
        self.health = 10
        self.attack = 5
        self.defense = 5
        self.special_attack = 5
        self.special_defense =5
        self.speed = 5

    def get_levelup_points(self):
        if self.level < 10 and self.level >= 5:
            return 1

        level_ratio = (self.level) / 100.0
        return int(level_ratio * 10)