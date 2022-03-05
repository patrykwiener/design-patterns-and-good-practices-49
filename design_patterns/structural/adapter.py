from abc import ABC, abstractmethod


class Service:
    def service_method(self, data):
        return 'response'


class AdapterInterface(ABC):

    @abstractmethod
    def send_converted(self, data):
        pass


class Adapter(AdapterInterface):

    def __init__(self, adaptee: Service):
        self._adaptee = adaptee

    def _convert_to_service_format(self, data):
        # performs conversion
        return data

    def send_converted(self, data):
        # some operations to convert data
        # e.g.:
        converted_data = self._convert_to_service_format(data)
        return self._adaptee.service_method(converted_data)


if __name__ == '__main__':
    service = Service()
    adapter = Adapter(service)

    data = {}
    service_response = adapter.send_converted(data)
