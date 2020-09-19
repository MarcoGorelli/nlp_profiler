from nlp_profiler.core \
    import NOT_APPLICABLE, gather_punctuations, count_punctuations  # noqa
import numpy as np
import pytest

text_with_punctuations = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."

text_to_return_value_mapping = [
    (np.nan, []),
    (float('nan'), []),
    (None, []),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_value_mapping)
def test_given_invalid_text_when_parsed_then_return_empty_list(
        text: str, expected_result: list
):
    # given, when
    actual_result = gather_punctuations(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


text_to_return_count_mapping = [
    (np.nan, NOT_APPLICABLE),
    (float('nan'), NOT_APPLICABLE),
    (None, NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_result",
                         text_to_return_count_mapping)
def test_given_invalid_text_when_counted_then_return_NOT_APPLICABLE(
        text: str, expected_result: list
):
    # given, when
    actual_result = count_punctuations(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_with_punctuations_when_parsed_then_return_only_punctuations():
    # given
    expected_results = ["'", ',', '-', '(', ';', ')', '.']

    # when
    actual_results = gather_punctuations(text_with_punctuations)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected punctuations in the text"


def test_given_a_text_with_punctuations_when_counted_then_return_count_of_punctuations():
    # given, when
    actual_results = count_punctuations(text_with_punctuations)

    # then
    assert actual_results == 7, \
        "Didn't find the expected number of punctuation marks in the text"
