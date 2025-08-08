from sklearn.linear_model import LogisticRegression
import random
x = [[1],[2],[3],[4],[5]]
y = [[0],[0],[0],[1],[1]]

model = LogisticRegression()

model.fit(x,y)

prediction = model.predict([[random.randint(0,5)]])

print(f"Will Be Student is Pass or Fail? ", "Yes" if prediction[0] == 1 else "No")