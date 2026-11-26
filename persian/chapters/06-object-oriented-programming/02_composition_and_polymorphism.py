class EmailChannel:
    def send(self, message: str) -> int:
        return len(message) * 2

class SmsChannel:
    def send(self, message: str) -> int:
        return len(message) * 5

class NotificationService:
    def __init__(self, channel: object) -> None:
        self.channel = channel

    def estimate_cost(self, message: str) -> int:
        return self.channel.send(message)

for channel in (EmailChannel(), SmsChannel()):
    print(NotificationService(channel).estimate_cost("Hello"))
