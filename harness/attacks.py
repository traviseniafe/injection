from dataclasses import dataclass

@dataclass(frozen=True)
class AttackCase:
    id: str
    category: str
    prompt: str
    expected_behavior: str