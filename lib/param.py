from enum import Enum


PARAM_FLOAT = 1
PARAM_OPTION = 2
PARAM_COLOR = 3
PARAM_POINT = 4


class Param:
    def __init__(self, type, name):
        self.type = type
        self.name = name


class FloatParam(Param):
    def __init__(self, name, min_value=0.0, max_value=1.0, default=0.5):
        self.min_value = min_value
        self.max_value = max_value
        self.default = default
        self.value = default
        super().__init__(PARAM_FLOAT, name)


class OptionParam(Param):
    def __init__(self, name, default=False):
        self.default = default
        self.value = default
        super().__init__(PARAM_OPTION, name)


class ColorParam(Param):
    def __init__(self, name, default=[1, 0, 0, 1]):
        self.default = default
        self.value = default
        super().__init__(PARAM_COLOR, name)


class PointParam(Param):
    def __init__(self, name, default=[0, 0]):
        self.default = default
        self.value = default
        super().__init__(PARAM_POINT, name)
