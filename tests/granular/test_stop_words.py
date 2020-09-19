from nlp_profiler.core \
    import NOT_APPLICABLE, gather_stop_words, count_stop_words  # noqa
import numpy as np
import pytest

text_with_a_number = '2833047 people live in this area'

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
    actual_result = gather_stop_words(text)

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
    actual_result = count_stop_words(text)

    # then
    assert expected_result == actual_result, \
        f"Expected: {expected_result}, Actual: {actual_result}"


def test_given_a_text_with_stop_words_when_parsed_then_return_only_the_stop_words():
    # given
    expected_results = ['in', 'this']

    # when
    actual_results = gather_stop_words(text_with_a_number)

    # then
    assert expected_results == actual_results, \
        "Didn't find the expected words in the text"


def test_given_a_text_with_stop_words_when_counted_then_return_count_of_stop_words():
    # given, when
    actual_results = count_stop_words(text_with_a_number)

    # then
    assert actual_results == 2, \
        "Didn't find the expected number of words in the text"
