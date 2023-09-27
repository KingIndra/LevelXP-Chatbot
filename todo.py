import requests, os

class TodoAPI:

    def __init__(self) -> None:
        self.url = os.environ.get("TODO_URL")
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "x-api-key": os.environ.get("TODO_KEY")
        }
        
    # routing
    def route(self, uid, message:str, type):
        uid = str(uid)

        if type == "create":
            textArr = message.split(",")
            id = textArr[0]
            task = "".join(textArr[1:])
            return self.create(uid, id, task)

        elif type == "read":
            return self.read(uid)

        elif type == "delete":
            return self.delete(uid, message)
        
        return "Error!"
    
    # creating
    def create(self, uid: str, id: str, task: str):
        data = {
            "type": "create", 
            "uid" : uid, 
            "id"  : id, 
            "task": task,
            "done": False
        }
        response = requests.get(self.url, headers = self.headers, json = data)
        return "created"
    
    # reading
    def read(self, uid: str):
        data = {
            "type": "read", 
            "uid" : uid
        }
        response = requests.get(self.url, headers = self.headers, json = data)
        res = response.json()
        message = "TASKS"
        for task in res:
            message += f"\n{task['id']}. {task['task']}"
        return message
    
    # deleting
    def delete(self, uid: str, id: str):
        data = {
            "type": "delete", 
            "uid" : uid, 
            "id"  : id
        }
        response = requests.get(self.url, headers = self.headers, json = data)
        return "deleted"