from entity import Entity


player = Entity(
    char="@",
    color=(255, 255, 255),
    name="Player",
    blocks_movement=True,
)

goblin = Entity(
    char="g",
    color=(0, 127, 0),
    name="Goblin",
    blocks_movement=True,
)

orc = Entity(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    blocks_movement=True,
)
