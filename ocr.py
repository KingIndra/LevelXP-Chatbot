import requests, os


class TextractAPI:

    def __init__(self) -> None:
        self.url = os.environ.get("OCR_URL")
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + os.environ.get("OCR_KEY")
        }
        
    def textrack(self, uid, image):
        data = {
            "user": uid,
            "base64": image
        }
        response = requests.get(self.url, headers = self.headers, json = data)
        return response
