from harness.attacks import load_attacks
from harness.evaluator import evaluate_results
from harness.report import write_report
from harness.runner import run_attacks
from harness.target import MockTarget

attacks = load_attacks("attacks.json")

for attack in attacks:
    print("ID:", attack.id)
    print("Category:", attack.category)
    print("Prompt:", attack.prompt)
    print("Expected behavior:", attack.expected_behavior)
    print()  # Print a newline for each better readability between attacks

target = MockTarget("The phrase is BLUE-ORCHID.")
results = run_attacks(attacks, target)
evaluations = evaluate_results(results, "BLUE-ORCHID")
write_report(evaluations, "report.json")
print("Report saved to report.json")