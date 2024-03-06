import os

import pytest
from guardrails import Guard
from validator import QARelevanceLLMEval

# Create a guard object
guard = Guard.from_string(
    validators=[QARelevanceLLMEval(llm_callable="gpt-3.5-turbo", on_fail="exception")]
)


@pytest.mark.skipif(
    os.environ.get("OPENAI_API_KEY") in [None, "mocked"],
    reason="openai api key not set",
)
@pytest.mark.parametrize(
    "test_output, metadata",
    [
        (
            "Jefferson City is the capital of Missouri.",
            {
                "original_prompt": "Write a sentence about any capital city in the U.S.",
                "pass_on_invalid": True,
            },
        ),
        (
            "Tenet",
            {
                "original_prompt": "What is the name of Christopher Nolan's latest movie?",
                "pass_on_invalid": True,
            },
        ),
    ],
)
def test_pass(test_output, metadata):
    result = guard.parse(test_output, metadata=metadata)

    assert result.validation_passed is True
    assert result.validated_output == test_output


@pytest.mark.skipif(
    os.environ.get("OPENAI_API_KEY") in [None, "mocked"],
    reason="openai api key not set",
)
def test_fail_non_responsive():
    with pytest.raises(Exception) as excinfo:
        guard.parse(
            "Paris is one of the most beautiful cities in the world.",
            metadata={
                "original_prompt": "Is the Computer Science program at MIT good?"
            },
        )  # Should fail, because the answer is irrelevant to the prompt.

    # Sometimes this test will fail bc the llm is unsure.
    assert str(excinfo.value) in (
        "Validation failed for field with errors: The LLM says 'No'. The validation failed.",
        "The LLM returned an invalid answer. Failing the validation...",
    )
