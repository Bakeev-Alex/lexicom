from redis import Redis


class RedisTools:
    """Класс подключения к кэшу redis."""

    __redis_connect = Redis(host="redis", port=6379)

    @classmethod
    def set_data(cls, key: str, value: str) -> None:
        """Метод записи и обновление данных в кэше."""

        cls.__redis_connect.set(key, value)
        return cls.__redis_connect.set(key, value)

    @classmethod
    def get_data(cls, key):
        """Метод получения данных из кэша."""
        # FixMe: посмотреть, что здесь возращается
        return cls.__redis_connect.get(key)

    @classmethod
    def get_all_keys(cls):
        return cls.__redis_connect.keys()
