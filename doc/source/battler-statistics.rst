Battler Statistics
=====================================
All battlers start out with the same base statistics, as listed below:

* Health: 10
* Attack: 5
* Defense: 5
* Special Attack: 5
* Special Defense: 5
* Speed: 5

Starting at level 5, A battler will gain an increasing number of stat points every level up.

The algorithm for the number of stat points given for a single level is very simple, and is as follows:

| (level / 100) * 10
| Exception: Levels 5-9 All give a flat 1 stat point, as the algorithm does for 10-19 (this allows for a clean stat point total, as well as avoids a long ramp up to start earning points).

This yields a clean total of 500 stat points for a max level 100 battler (including the 35 base stats)

Stat points are distributed to any of the battler's stats at will by the trainer, with a single caveat:
#. Any individual stat of a battler cannot exceed 255 (260 for health) (this would be half of the alloted battle points for a single battler)
