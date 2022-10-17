from classes.PersonInfo import PersonInfo


class EndpointFactory:
    _ENDPOINT_MAP = {
        'PersonInfo': PersonInfo
    }

    def __init__(self, params: dict):
        self._check_params(params)
        self._extract_params(params)

    def _check_params(self, params: dict):
        if not params:
            params = {}

        self._endpoint_name = params.get('endpointName')
        self._method_name = params.get('method')

        if not self._endpoint_name:
            raise RuntimeError('Не передано название конечной точки')

        if self._endpoint_name not in self._ENDPOINT_MAP:
            raise RuntimeError(f'Конечная точка {self._endpoint_name} не поддерживается')

        if not self._method_name:
            raise RuntimeError('Не передано название метода')

        if self._method_name not in self._ENDPOINT_MAP[self._endpoint_name].methods_map:
            raise RuntimeError(f'Метод {self._method_name} не поддерживается сущностью {self._endpoint_name}')

    def _extract_params(self, params: dict):
        self._endpoint = self._ENDPOINT_MAP[self._endpoint_name]
        self._method = self._endpoint.methods_map[self._method_name]

        data = params.get('data') or {}

        self._filter = data.get('filter')
        self._data_params = data.get('params')

    def process(self):
        return self._method(data=self._data_params, filter=self._filter)
