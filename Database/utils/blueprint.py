from flask import Blueprint as NewBlueprint


class Blueprint:
    def __new__(cls, blueprint_name: str) -> None:
        return NewBlueprint(
            blueprint_name,
            __name__,
        )
