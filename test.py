import pandas as pd
score = pd.read_csv('exam_score.csv')
print(score.head(5))
print(score.describe())

