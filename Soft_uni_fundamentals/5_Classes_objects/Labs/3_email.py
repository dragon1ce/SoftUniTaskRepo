class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_list = []
indices = []

while True:
    entry = input()
    if entry == "Stop":
        break
    sender, receiver, content = entry.split()
    email = Email(sender, receiver, content)
    email_list.append(email)

indices = [int(i) for i in input().split(", ")]
for item in indices:
    if item in range(len(email_list)):
        email_list[item].send()
for i in email_list:
    print(Email.get_info(i))
