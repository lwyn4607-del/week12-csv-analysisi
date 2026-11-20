import pandas as pd

from analysis import (
    정제,
    반별평균,
    CLASS_COL,
    SCORE_COL
)

df = 정제(pd.read_csv("scores_2026.csv"))
mini = 정제(pd.read_csv("mini.csv"))


# Test 1: Final rows must be 100
def test_clean_data_100_rows():
    assert len(df) == 100


# Test 2: Two classes must exist
def test_two_classes():
    assert sorted(df[CLASS_COL].unique()) == ["1반", "2반"]


# Test 3: Total scores must match
def test_total_score():
    assert (
        df.groupby(CLASS_COL)[SCORE_COL].sum().sum()
        == df[SCORE_COL].sum()
    )


# Test 4: Mini data average
def test_mini_average():
    assert 반별평균(mini)["1반"] == 80.0