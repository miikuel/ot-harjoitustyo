
class Task:

    def __init__(self, topic, category, deadline, task_id=None, done=False):
        self.topic = topic
        self.category = category
        self.deadline = deadline
        self.task_id = task_id
        self.done = done
