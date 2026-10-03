from harness.attacks import load_attacks

attacks = load_attacks("attacks.json")

for attack in attacks:
    print("ID:", attack.id)
    print("Category:", attack.category)
    print("Prompt:", attack.prompt)
    print("Expected behavior:", attack.expected_behavior)
    print()  # Print a newline for each better readability between attacks