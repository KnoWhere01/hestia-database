import importlib
from os import scandir


def set_routes(app):
    for item in scandir("routes"):
        if item.is_dir() and "__pycache__" not in item.name:
            for file in ["create", "delete", "read", "update"]:
                locals()[f"{item.name}_{file}"] = importlib.import_module(
                    f"routes.{item.name}.{file}"
                )
                app.register_blueprint(
                    getattr(locals()[f"{item.name}_{file}"], "blueprint")
                )

    return True
