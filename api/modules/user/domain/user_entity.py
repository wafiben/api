


from api.modules.user.domain.value_objects.user_id import UserId


class UserEntity:
    def __init__(self, id: UserId, first_name: str, last_name: str, city: str, age: int):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._city = city
        self._age = age

    @staticmethod
    def create(create: dict) -> 'UserEntity':
        id = UserId.generate()
        first_name = create['firstName']
        last_name = create['lastName']
        city = create['city']
        age = create['age']
        user_entity = UserEntity(id, first_name, last_name, city, age)
        return user_entity
