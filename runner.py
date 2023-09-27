import requests, os


class ScriptRunner:

    def __init__(self) -> None:
        self.url = os.environ.get("RUNNER_URL")
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "x-api-key": os.environ.get("RUNNER_KEY")
        }
        
    def execute(self, uid, code, exe):
        data = {
            "user": uid,
            "language": exe,
            "code": code
        }
        response = requests.get(self.url, headers = self.headers, json = data)
        return response
    