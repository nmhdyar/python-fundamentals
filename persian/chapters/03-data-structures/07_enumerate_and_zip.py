names = ["آوا", "مینا", "نوح"]
scores = [18, 20, 17]

for index, name in enumerate(names, start=1):
    print(index, name)

for name, score in zip(names, scores):
    print(f"{name}: {score}")
