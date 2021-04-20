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


# return [
# "step": FloatParam()
# ["Step", "step", "float", 0.0, 1.0, 0.5],
# ["Option A", "option_a", "bool", 0.0, 1.0, False],
# ["Color A", "color_a", "color", 0.0, 1.0, [1, 0, 0, 1]],
# ["Point A", "point_a", "point", 0.0, 1.0, [0.5, 0.5]],
# ]

# AE interogates params to bind UI
# on render, AE invokes params array and updates all values in array instead of polluting var space
# can make a function that updates param value