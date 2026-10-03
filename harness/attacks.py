import json
from dataclasses import dataclass

@dataclass(frozen=True)
class AttackCase:
    id: str
    category: str
    prompt: str
    expected_behavior: str

def load_attacks(path:str) -> list[AttackCase]:
    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    attacks = []

    seen_ids = set()
    
    for item in data:
        if item["id"] in seen_ids:
            raise ValueError("Duplicate attack ID found:", item["id"])
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
    