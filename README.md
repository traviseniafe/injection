# Prompt Injection Test Harness

> **Status:** In progress

## Problem

AI systems can be targeted with prompts that try to override their instructions or extract information. This project tests common direct prompt-injection attempts and records how a target responds.

## Intended audience

Developers and security testers evaluating AI systems they are authorized to test.

## Version 0.1 scope

### In scope

- Single-turn, direct text prompts.
- Attempts to override instructions and extract a known test phrase.
- A mock target for repeatable local runs.
- An OpenAI Responses API adapter.
- Exact-phrase, case-insensitive evaluation.
- JSON reports and a command-line interface.

### Out of scope

- Indirect injections hidden in webpages, documents, or tool results.
- Multi-turn attacks.
- Image-based attacks.
- LLM-as-judge evaluation.
- Testing multiple targets at once.
- Determining whether an attack would work against a separate application that this harness is not connected to.

## Design

```text
attacks.json → Attack loader → Runner → Target → Response
                                    ↓              ↓
                                 Test result → Evaluator → JSON report
```

| Component | Responsibility | Status |
|---|---|---|
| Attack library | Load and validate JSON attack cases | Implemented |
| Mock target | Return a chosen response for local tests | Implemented |
| OpenAI target | Send one prompt with test instructions through the Responses API | Implemented; covered with a fake-client test; live response not yet verified |
| Runner | Send each attack and associate its response with the attack ID | Implemented |
| Evaluator | Check responses for the protected phrase | Implemented |
| JSON report | Save outcomes to a JSON file | Implemented |
| CLI | Choose the target, attack file, model, and report path | Implemented |

## Setup

Use Python 3 and a virtual environment, then install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Run with the mock target

The mock target is the default and makes no API request:

```bash
python -m harness.cli --protected-text BLUE-ORCHID --limit 1
```

To simulate a response containing the test phrase:

```bash
python -m harness.cli --protected-text BLUE-ORCHID --mock-response "The phrase is BLUE-ORCHID." --limit 1
```

Both commands write `report.json` in the current directory. That generated file is ignored by Git.

## Run with the OpenAI target

Set `OPENAI_API_KEY` in your environment, then run:

```bash
python -m harness.cli --target openai --protected-text BLUE-ORCHID --limit 1
```

Each attack makes one API request and may incur usage charges. Use test phrases only. The current OpenAI adapter sends the test instructions created by the CLI; it does not connect to a separate chatbot or retrieve that chatbot's private system instructions.

## Run tests

```bash
python -m unittest discover -s tests
```

The OpenAI adapter test uses a fake client, so the test suite does not make API calls.

## Interpreting results

- `possible_leak` means the response contained the configured protected phrase.
- `no_leak_detected` means this exact-phrase check did not find it.

The evaluator currently performs only a case-insensitive exact-phrase check. It does not understand paraphrases or determine whether the model followed its instructions in other ways. A `no_leak_detected` result is not proof that a system is secure.

## Roadmap

- [x] Load and validate attack cases.
- [x] Add a repeatable mock target.
- [x] Add an OpenAI Responses API target adapter.
- [x] Run attacks, evaluate exact canary phrases, and write JSON reports.
- [x] Add a command-line interface.
- [ ] Verify the OpenAI adapter with a successful live API request.
- [ ] Explore indirect-injection tests in a controlled document or tool environment.
- [ ] Improve evaluation beyond exact phrase matching.

## What I learned

_Write this section in your own words as the project develops._
