def forward_chaining(rules, facts):
    while True:
        new_facts = set()
        for rule in rules:
            antecedent, consequent = rule
            if all(fact in facts for fact in antecedent):
                new_facts.add(consequent)
        if not new_facts:
            break
        facts.update(new_facts)
    return facts

# Example Knowledge Base
rules = [
    (("A", "B"), "C"),
    ("A", "D"),
    ("D", "E")
]

# Initial Facts
facts = {"A", "B"}

# Perform forward chaining
result = forward_chaining(rules, facts)
print(result)  # Output: {'A', 'B', 'C', 'D', 'E'}
