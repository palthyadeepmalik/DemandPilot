class UnitConverter:

    @staticmethod
    def to_base(quantity: float, unit: str):

        unit = unit.lower()

        conversions = {
            "g": quantity / 1000,
            "kg": quantity,
            "ml": quantity / 1000,
            "l": quantity,
            "base": quantity,
            "piece": quantity,
        }

        return conversions.get(unit, quantity)

    @staticmethod
    def base_unit(unit: str):

        unit = unit.lower()

        if unit in ["g", "kg"]:
            return "kg"

        if unit in ["ml", "l"]:
            return "l"

        return unit