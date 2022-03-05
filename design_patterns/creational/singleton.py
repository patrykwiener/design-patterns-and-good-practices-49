class Singleton:
    _INSTANCE = None

    _DB_PORT = 3467

    def __init__(self):
        raise NotImplementedError('Creation of singleton instance with constructor is forbidden')

    @classmethod
    def get_instance(cls):
        if cls._INSTANCE is None:
            cls._INSTANCE = cls.__new__(cls)
        return cls._INSTANCE

    def get_db_port(self):
        return self._DB_PORT


if __name__ == '__main__':
    instance_1 = Singleton.get_instance()
    instance_2 = Singleton.get_instance()
    assert instance_1 is instance_2
