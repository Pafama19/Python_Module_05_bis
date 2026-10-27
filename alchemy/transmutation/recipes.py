
from alchemy.elements import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    """Transmute lead into gold."""
    air: str = create_air()
    strength: str = strength_potion()
    fire: str = create_fire()

    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' "
        f"and '{strength}' mixed with '{fire}'"
    )
