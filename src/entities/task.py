
class Task:

    def __init__(self, topic, category, deadline, done=False, user=None):
        self.topic = topic
        self.category = category
        self.deadline = deadline
        self.done = done
        self.user = None