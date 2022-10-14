import importlib
from os import scandir


def set_routes(app):
    for item in scandir("routes"):
        if item.is_dir() and "__pycache__" not in item.name:
            locals()[item.name] = importlib.import_module(
                f"routes.{item.name}.{item.name}"
            )
            app.register_blueprint(getattr(locals()[item.name], "blueprint"))

    return True
