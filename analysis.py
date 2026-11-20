import pandas as pd
CLASS_COL = "반"
SUBJECT_COL = "과목"
SCORE_COL = "점수"


def 정제(df):
    정제된_df = df.copy()

    # 점수가 비어 있는 행을 삭제한다.
    정제된_df = 정제된_df.dropna(subset=["점수"])
    print(len(정제된_df))

    # 모든 열의 값이 같은 중복 행을 삭제한다.
    정제된_df = 정제된_df.drop_duplicates()
    print(len(정제된_df))

    # 반과 과목 값의 앞뒤 공백을 제거한다.
    정제된_df["반"] = 정제된_df["반"].str.strip()
    정제된_df["과목"] = 정제된_df["과목"].str.strip()
    print(len(정제된_df))

    # 점수가 0부터 100 사이가 아닌 행을 삭제한다.
    정제된_df = 정제된_df[정제된_df["점수"].between(0, 100)]
    print(len(정제된_df))

    return 정제된_df
# 반별 평균을 계산하는 함수
def 반별평균(df):
    return df.groupby(CLASS_COL)[SCORE_COL].mean().round(2)

if __name__ == "__main__":
    df = pd.read_csv("scores_2026.csv")
    df = 정제(df)
    수학_df = df[df["과목"] == "수학"]
    print("수학 데이터:")
    print(수학_df)
    print("수학 행 수:", len(수학_df))

    print(df.head())
    print(df.shape)

    # A. Subject filter
    print("과목별 데이터")
    print(df[df[SUBJECT_COL] == "을비"])

    # B. Class total score
    print("반별 총점")
    print(df.groupby(CLASS_COL)[SCORE_COL].sum())

    # C. Class and subject average
    print("반별 과목 평균")
    print(
        df.pivot_table(
            values=SCORE_COL,
            index=CLASS_COL,
            columns=SUBJECT_COL,
            aggfunc="mean"
        )
)

    # D. Statistics
    print("반별 통계")
    print(
        df.groupby(CLASS_COL)[SCORE_COL]
        .agg(["count", "sum", "mean", "min", "max"])
    )

     # E. Total verification
    print("전체 점수 합계:")
    print(df.groupby(CLASS_COL)[SCORE_COL].sum().sum())

    print(df[SCORE_COL].sum())

    print("전체 인원:")
    print(df.groupby(CLASS_COL)[SCORE_COL].count().sum())

    print(len(df))
mini = pd.read_csv("mini.csv")
mini = 정제(mini)

print("Mini data:")
print(mini)


