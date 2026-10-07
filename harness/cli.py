import argparse

from harness.attacks import load_attacks
from harness.evaluator import evaluate_results
from harness.report import write_report
from harness.runner import run_attacks
from harness.target import MockTarget

def main():
    parser = argparse.ArgumentParser(
        description="Run prompt-injection tests with a mock target."
    )

    parser.add_argument(
        "--attacks",
        default="attacks.json",
        help="Path to the JSON attack library.",
    )
    parser.add_argument(
        "--protected-text",
        required=True,
        help="Test phrase the target should keep private.",
    )
    parser.add_argument(
        "--output",
        default="report.json",
        help="Path where the JSON report will be saved."
    )
    parser.add_argument(
        "--mock-response",
        default="I will keep the phrase private.",
        help="Fixed response returned by the mock target.",
    )

    args = parser.parse_args()

    attacks = load_attacks(args.attacks)
    target = MockTarget(args.mock_response)
    results = run_attacks(attacks, target)
    evaluations = evaluate_results(results, args.protected_text)
    write_report(evaluations, args.output)

    print("Report saved to " + args.output)


if __name__ == "__main__":
    main()