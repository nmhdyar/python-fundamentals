class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print(list(Countdown(3)))
