
def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients against the light spellbook."""
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    ingredients_lower: str = ingredients.lower()

    for ingredient in allowed:
        if ingredient in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
