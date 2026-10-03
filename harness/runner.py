from dataclasses import dataclass

from harness.attacks import AttackCase


@dataclass(frozen=True)
class TestResult:
    attack_id: str
    category: str
    prompt: str
    expected_behavior: str
    response: str


def run_attacks(attacks: list[AttackCase], target) -> list[TestResult]:
    results = []

    for attack in attacks:
        response = target.respond(attack.prompt)

        result = TestResult(
            attack_id=attack.id,
            category=attack.category,
            prompt=attack.prompt,
            expected_behavior=attack.expected_behavior,
            response=response,
        )
        results.append(result)

    return results