class Message:
    def __init__(self, user, room, text, id=None, thread_id=None):
        self.user = user
        self.room = room
        self.text = text
        self.id = id
        self.thread_id = thread_id

    def was_sent_to(self, subject):
        if not self.text:
            return False

        tokens = self.text.lower().split(" ")
        if not tokens:
            return False

        first_token = tokens[0].lstrip(" @").rstrip(" :-=")
        return first_token == subject.lower()
