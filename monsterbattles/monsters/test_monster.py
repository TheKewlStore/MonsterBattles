from monster import Monster

monster = Monster('test', 'Fire')

total_stat_points = 35

for level in xrange(1, 101):
    monster.level = level
    print 'monster gains {0} stat points at level {1}'.format(monster.get_levelup_points(), level)
    total_stat_points += monster.get_levelup_points()
    
print total_stat_points
