import json
from dataclasses import dataclass

@dataclass(frozen=True)
class AttackCase:
    id: str
    category: str
    prompt: str
    expected_behavior: str

class AttackLibraryError(ValueError):
    pass # This exception is raised when there is an error in the attack library, such as a duplicate attack ID.

def load_attacks(path:str) -> list[AttackCase]:
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
    except OSError as error:
        raise AttackLibraryError(f"Could not read {path}: {error}") from error
    except json.JSONDecodeError as error:
        raise AttackLibraryError(f"Invalid JSON in {path}: {error}") from error
       
    if not isinstance(data, list):
        raise AttackLibraryError("The attack library must be a JSON list.")
    
    attacks = []
    seen_ids = set()
    required_fields = ("id", "category", "prompt", "expected_behavior")

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise AttackLibraryError(f"Attack at position {index} must be an object.")

        missing = [field for field in required_fields if field not in item]
        if missing:
            raise AttackLibraryError(
                f"Attack at position {index} is missing: {', '.join(missing)}"
            )

        for field in required_fields:
            value = item[field]
            if not isinstance(value, str) or not value.strip():
                raise AttackLibraryError(
                    f"Attack at position {index}: '{field}' must be a non-empty string."
                )

    for item in data:
        if item["id"] in seen_ids:
            raise AttackLibraryError("Duplicate attack ID found:", item["id"])
        else:
            seen_ids.add(item["id"])

        attack = AttackCase(
            id=item["id"],
            category=item["category"],
            prompt=item["prompt"],
            expected_behavior=item["expected_behavior"]
        )
        attacks.append(attack)

    return attacks