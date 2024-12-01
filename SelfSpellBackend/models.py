from firebase_admin import firestore

class Hobby:
    collection_name = "Hobbies"

    @classmethod
    def add_task(cls, data):
        db = firestore.client()
        task_ref = db.collection(cls.collection_name).add(data)
        return task_ref

    @classmethod
    def get_all_tasks(cls):
        db = firestore.client()
        tasks_ref = db.collection(cls.collection_name).stream()
        tasks = [{**task.to_dict(), 'id': task.id} for task in tasks_ref]
        return tasks
