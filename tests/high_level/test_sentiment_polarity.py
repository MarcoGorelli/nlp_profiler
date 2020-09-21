import math

import numpy as np
import pytest

from nlp_profiler.constants import NOT_APPLICABLE, NaN
from nlp_profiler.sentiment_polarity import sentiment_polarity_score, \
    sentiment_polarity_summarised, sentiment_polarity  # noqa

positive_text = "This sentence doesn't seem to too many commas, periods or semi-colons (;)."
negative_text = "2833047 people live in this area. It is not a good area."
neutral_text = "Today's date is 04/28/2020 for format mm/dd/yyyy, not 28/04/2020."

text_to_return_value_mapping = [
    (np.nan, NaN, NOT_APPLICABLE),
    (float('nan'), NaN, NOT_APPLICABLE),
    (None, NaN, NOT_APPLICABLE),
    ("", NaN, NOT_APPLICABLE),
]


@pytest.mark.parametrize("text,expected_score,expected_polarity",
                         text_to_return_value_mapping)
def test_given_an_invalid_text_when_sentiment_analysis_is_applied_then_no_sentiment_analysis_info_is_returned(
        text: str, expected_score: float, expected_polarity: str
):
    # given, when: text is not defined
    actual_score = sentiment_polarity_score(text)

    # then
    assert actual_score is expected_score, \
        f"Sentiment polarity score should NOT " \
        f"have been returned, expected {expected_score}"

    # given, when
    actual_polarity = sentiment_polarity(actual_score)

    # then
    assert actual_polarity == expected_polarity, \
        f"Sentiment polarity should NOT " \
        f"have been returned, expected {expected_polarity}"


def test_given_a_text_when_sentiment_analysis_is_applied_then_sentiment_analysis_info_is_returned():
    verify_text_polarity(positive_text, 0.375000, 'Pretty positive', 'Positive')
    verify_text_polarity(negative_text, -0.10681818181818181, 'Pretty negative', 'Negative')
    verify_text_polarity(neutral_text, 0.0, 'Neutral', 'Neutral')


def verify_text_polarity(text: str,
                         expected_polarity_score: float,
                         expected_polarity: str,
                         expected_polarity_summarised: str):
    # given, when
    actual_score = sentiment_polarity_score(text)
    # then
    if expected_polarity_score is NaN:
        assert actual_score is expected_polarity_score
    else:
        assert math.isclose(expected_polarity_score, actual_score,
                            rel_tol=1e-09, abs_tol=0.0), \
            "Sentiment polarity score didn't match for the text"

    # given, when
    actual_polarity = sentiment_polarity(actual_score)
    # then
    assert expected_polarity == actual_polarity, \
        "Sentiment polarity didn't match for the text"

    # given, when
    actual_summarised_polarity = sentiment_polarity_summarised(actual_polarity)
    # then
    assert expected_polarity_summarised == actual_summarised_polarity, \
        "Summarised Sentiment polarity didn't match for the text"


### The General Area of Possibility
### See https://en.wikipedia.org/wiki/Words_of_estimative_probability
sentiment_polarity_score_to_words_mapping = [
    (1, 0.99555, "Very positive"),  # ["Very positive", 99, 100],  # Certain: 100%: Give or take 0%
    (0.99, 0.99555, "Very positive"),  # ["Very positive", 99, 100],  # Certain: 100%: Give or take 0%
    (0.95, 0.95, "Quite positive"),  # ["Quite positive", 87, 99],  # Almost Certain: 93%: Give or take 6%
    (0.60, 0.60, "Pretty positive"),  # ["Pretty positive", 51, 87],  # Probable: 75%: Give or take about 12%
    (0.0, 0.50, "Neutral"),  # ["Neutral", 49, 51],  # Chances About Even: 50%: Give or take about 10%
    (-0.60, 0.30, "Pretty negative"),  # ["Pretty negative", 12, 49],  # Probably Not: 30%: Give or take about 10%
    (-0.95, 0.08, "Quite negative"),  # ["Quite negative", 2, 12],  # Almost Certainly Not 7%: Give or take about 5%
    (-0.99, 0.01, "Very negative"),  # ["Very negative", 0, 2]  # Impossible 0%: Give or take 0%
    (-1, 0.01, "Very negative"),  # ["Very negative", 0, 2]  # Impossible 0%: Give or take 0%
]


@pytest.mark.parametrize("original_score,normalised_score,expected_sentiment_in_words",
                         sentiment_polarity_score_to_words_mapping)
def test_given_sentiment_polarity_score_when_converted_to_words_then_return_right_word(
        original_score: float, normalised_score: float, expected_sentiment_in_words: str
):
    # given, when
    print("original_score:", original_score,
          "normalised_score: ", normalised_score,
          "expected_sentiment_in_words:", expected_sentiment_in_words)
    actual_result = sentiment_polarity(original_score)

    # then
    assert expected_sentiment_in_words == actual_result
