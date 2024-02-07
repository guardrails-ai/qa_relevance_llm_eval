## Details

| Developed by | Guardrails AI |
| --- | --- |
| Date of development | Feb 15, 2024 |
| Validator type | Chatbots, QA |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

## Description

This validator checks whether an answer is relevant to the question asked by asking the LLM to self evaluate.

## Example Usage Guide

### Installation

```bash
$ gudardrails hub install qa-relevance-llm-eval
```

### Initialization

```python
qa_relevance_validator = QARelevanceLLMEval(
	llm_callable="openai",
	on_fail="noop")

# Create Guard with Validator
guard = Guard.from_string(
    validators=[qa_relevance_validator, ...],
    num_reasks=2,
)
```

### Invocation

```python
guard(
    "LLM response",
    metadata={"question": "The question asked to the LLM"}
)
```

## Intended use

- Primary intended uses: This validator is primarily useful when building chatbots.
- Out-of-scope use cases:

## Expected deployment metrics

|  | CPU | GPU |
| --- | --- | --- |
| Latency |  | - |
| Memory |  | - |
| Cost |  | - |
| Expected quality |  | - |

## Resources required

- Dependencies: Foundation model
- Foundation model access keys: Foundation model access keys
- Compute: na

## Validator Performance

### Evaluation Dataset

### Model Performance Measures

| Accuracy |  |
| --- | --- |
| F1 Score |  |

### Decision thresholds
