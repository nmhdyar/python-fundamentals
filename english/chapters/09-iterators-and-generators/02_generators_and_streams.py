def even_squares(limit: int):
    for number in range(limit):
        if number % 2 == 0:
            yield number * number


pipeline = (value + 1 for value in even_squares(6))
print(list(pipeline))
