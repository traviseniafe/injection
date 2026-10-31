from dataclasses import dataclass

from harness.attacks import AttackCase


@dataclass(frozen=True)
class TestResult:
    attack_id: str
    category: str
    prompt: str
    expected_behavior: str
    response: str
    untrusted_content: str = ""


def run_attacks(attacks: list[AttackCase], target) -> list[TestResult]:
    results = []

    for attack in attacks:
        prompt = attack.prompt
        if attack.untrusted_content:
            prompt = (
                attack.prompt + "\n\nUntrusted content to summarize:\n" + attack.untrusted_content
            )
        response = target.respond(prompt)

        result = TestResult(
            attack_id=attack.id,
            category=attack.category,
            prompt=attack.prompt,
            expected_behavior=attack.expected_behavior,
            response=response,
            untrusted_content=attack.untrusted_content
        )
        results.append(result)

    return results