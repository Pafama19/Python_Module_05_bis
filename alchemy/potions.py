
from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    """Brew a healing potion using earth and air."""
    earth: str = create_earth()
    air: str = create_air()
    return (
        f"Healing potion brewed with '{earth}' and '{air}'"
    )


def strength_potion() -> str:
    """Brew a strength potion using fire and water."""
    fire: str = create_fire()
    water: str = create_water()
    return (
        f"Strength potion brewed with '{fire}' and '{water}'"
    )
