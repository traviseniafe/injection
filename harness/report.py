import json


def write_report(evaluations: list[dict], path: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(evaluations, file, indent=2)