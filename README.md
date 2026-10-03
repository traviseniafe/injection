# Prompt Injection Test Harness

> **Status:** In Progress

## Problem

AI systems can be targeted with prompts that try to override their instructions or extract information. This project tests common direct prompt-injection attempts and records how a target responds.

## Intended audience

Developers and security testers evaluating AI systems they are authorized to test.

## Scope

### Version 0.1

- Test single-turn, direct text prompts.
- Include attempts to override instructions and extract protected information.
- Evaluate responses with simple, documented rules.
- Save results as JSON.

### Out of scope for version 0.1

- Indirect injections hidden in webpages, documents, or tool results.
- Multi-turn attacks.
- Image-based attacks.
- LLM-as-judge evaluation.
- Testing multiple targets at once.

## How results should be interpreted

A rule match is evidence that a response may have followed an attack. A rule match is not proof that the target is insecure, and no match is not proof that it is secure. The evaluator will report what it observed and which rule matched.

For hidden-instruction tests, the initial evaluator may flag a response that claims to reveal instructions or contains a known test phrase. These outcomes should be described as possible leakage unless the phrase is confirmed to be protected content.

## Design

```text
Attack cases → Runner → Target system → Response
                   ↓                       ↓
                Test record ← Evaluator
                   ↓
               JSON report
```

| Component | Responsibility | Status |
|---|---|---|
| Attack library | Store prompts, categories, and expected behavior | Planned |
| Runner | Send each prompt to the target | Planned |
| Target adapter | Provide a consistent way to call a target | Planned |
| Evaluator | Apply documented rules to responses | Planned |
| JSON report | Summarize each test and the overall run | Planned |
| CLI | Run the harness from a terminal | Planned |

## Roadmap

- [ ] Define and load attack cases
- [ ] Add a mock target for repeatable local runs
- [ ] Evaluate responses with simple rules
- [ ] Write JSON reports
- [ ] Add a command-line interface
- [ ] Explore indirect injection tests for a later version
- [ ] Consider stronger evaluation using known canary phrases
