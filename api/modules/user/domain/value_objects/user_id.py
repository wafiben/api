import uuid

class UserId:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def generate() -> 'UserId':
        generated_uuid = uuid.uuid4()  
        return UserId(str(generated_uuid)) 