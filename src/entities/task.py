
class Task:

    """Luokka, joka kuvaa yksittäistä tehtävää.

    Attributes:
        topic: merkkijono, joka kuvaa tehtävän otsikkoa.
        category: merkkijono, joka kuvaa tehtävän kategoriaa.
        deadline: merkkijono, joka kuvaa tehtävän määräpäivää.
        task_id: tehtävän yksilöivä id tietokannassa.
        done: boolean, joka kuvaa onko tehtävä tehty.
    """

    def __init__(self, topic, category, deadline, task_id=None, done=False):
        self.topic = topic
        self.category = category
        self.deadline = deadline
        self.task_id = task_id
        self.done = done
