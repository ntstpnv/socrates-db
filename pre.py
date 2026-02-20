from pathlib import Path


def walk_package(path: Path, ignore: set, prefix: str = "") -> None:

    elements = sorted(
        (el for el in path.iterdir() if el.name not in ignore),
        key=lambda el: (not el.is_dir(), el.name),
    )

    count = len(elements)

    for i, el in enumerate(elements):
        last = i == count - 1

        tree.write(f"{prefix}{'└── ' if last else '├── '}{el.name}\n")

        if el.is_dir():
            walk_package(el, ignore, prefix + ("    " if last else "│   "))
        else:
            with open(el, encoding="utf-8") as file:
                data.write(f"{el}\n\n{file.read()}\n\n")


if "__main__" == __name__:
    PACKAGE = "maxapi"
    BASE_DIR = Path(__file__).resolve().parent

    PATH = BASE_DIR / ".venv" / "Lib" / "site-packages" / PACKAGE
    IGNORE = {"__pycache__", "*.pyc"}

    with (
        open("tree.txt", "w", encoding="utf-8") as tree,
        open("data.txt", "w", encoding="utf-8") as data,
    ):
        walk_package(PATH, IGNORE)
