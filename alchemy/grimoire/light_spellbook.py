
def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell if its ingredients are valid."""
    from .light_validator import validate_ingredients

    validation: str = validate_ingredients(ingredients)

    if "VALID" in validation and "INVALID" not in validation:
        return f"Spell recorded: {spell_name} ({validation})"

    return f"Spell rejected: {spell_name} ({validation})"
