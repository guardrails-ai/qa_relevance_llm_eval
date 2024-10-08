## Overview

| Developed by | Guardrails AI |
| Date of development | Feb 15, 2024 |
| Validator type | Chatbots, QA |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

## Description

This validator checks whether an answer is relevant to the question asked by asking the LLM to self evaluate.

### Intended use

The primary intended uses is for building chatbots, and verifying answer relevance for chatbots.

### Requirements

* Dependencies: 
    - Foundation model access (any LLM provider supported by LiteLLM)
    - guardrails-ai>=0.4.0

## Installation

```bash
$ guardrails hub install hub://guardrails/qa_relevance_llm_eval
```

## Usage Examples

### Validating string output via Python

In this example, we apply the validator to a string output generated by an LLM.

```python
# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import QARelevanceLLMEval

# Setup Guard
guard = Guard().use(
    QARelevanceLLMEval,
    llm_callable="gpt-3.5-turbo",
    on_fail="exception",
)

res = guard.validate(
    "Jefferson City is the capital of Missouri.",
    metadata={
        "original_prompt": "Tell me about any capital city in the U.S.",
        "pass_on_invalid": True,
    },
)  # Validation passes
try:
    res = guard.validate(
        """
        Inception is a 2010 science fiction action film written and directed by Christopher Nolan. 
        It stars Leonardo DiCaprio as a professional thief who steals information 
        by infiltrating the subconscious of his targets.
        """,
        metadata={
            "original_prompt": """IKEA is a Swedish company, founded in 1943 by Ingvar Kamprad, 
            that designs and sells ready-to-assemble furniture, kitchen appliances and home accessories.
            """,
        },
    )  # Validation fails
except Exception as e:
    print(e)
```
Output:
```console
Validation failed for field with errors: The LLM says 'No'. The validation failed.
```

# API Reference

**`__init__(self, llm_callable="gpt-3.5-turbo", on_fail="noop")`**
<ul>

Initializes a new instance of the Validator class.

**Parameters:**

- **`llm_callable`** _(str):_ Model name to make the LiteLLM call. Defaults to gpt-3.5-turbo.
- **`on_fail`** *(str, Callable):* The policy to enact when a validator fails. If `str`, must be one of `reask`, `fix`, `filter`, `refrain`, `noop`, `exception` or `fix_reask`. Otherwise, must be a function that is called when the validator fails.

</ul>

<br/>

**`validate(self, value, metadata={}) -> ValidationResult`**

<ul>

Validates the given `value` using the rules defined in this validator, relying on the `metadata` provided to customize the validation process. This method is automatically invoked by `guard.parse(...)`, ensuring the validation logic is applied to the input data.

Note:

1. This method should not be called directly by the user. Instead, invoke `guard.parse(...)` where this method will be called internally for each associated Validator.
2. When invoking `guard.parse(...)`, ensure to pass the appropriate `metadata` dictionary that includes keys and values required by this validator. If `guard` is associated with multiple validators, combine all necessary metadata into a single dictionary.

**Parameters:**

- **`value`** *(Any):* The input value to validate.
- **`metadata`** *(dict):* A dictionary containing metadata required for validation. - Keys and values must match the expectations of this validator.
    
    
    | Key | Type | Description | Required| Default |
    | --- | --- | --- | --- | --- |
    | `original_prompt` | _str_ | The original prompt the LLM is supposedly responding to. | Yes | None |

</ul>
