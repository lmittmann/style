import sys


_enabled = sys.stdout.isatty()
_styles = {
    'bold': 1,
    'dim': 2,
    'italic': 3,
    'underline': 4,
    'inverse': 7,
    'hidden': 8,
    'strikethrough': 9,
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
    'light_black': 90,
    'light_red': 91,
    'light_green': 92,
    'light_yellow': 93,
    'light_blue': 94,
    'light_magenta': 95,
    'light_cyan': 96,
    'light_white': 97,
    'on_black': 40,
    'on_red': 41,
    'on_green': 42,
    'on_yellow': 43,
    'on_blue': 44,
    'on_magenta': 45,
    'on_cyan': 46,
    'on_white': 47,
    'on_light_black': 100,
    'on_light_red': 101,
    'on_light_green': 102,
    'on_light_yellow': 103,
    'on_light_blue': 104,
    'on_light_magenta': 105,
    'on_light_cyan': 106,
    'on_light_white': 107
}


class StyleBuilder:
    def __init__(self, style_list, is_root=False):
        self._style_list = style_list
        self._is_root = is_root

    def __call__(self, *objects, **kwargs):
        sep = kwargs.get('sep', ' ')
        if type(sep) is not str:
            raise TypeError('sep must be None or a string, not %s' % type(sep).__name__)

        string = sep.join(str(obj) for obj in objects)
        if _enabled and self._style_list:
            return '\033[%sm%s\033[0m' % (';'.join([str(val) for val in self._style_list]), string)
        return string

    def __getattr__(self, attr):
        if attr in _styles:
            if self._is_root:
                new_style_list = self._style_list[:]
                new_style_list.append(_styles[attr])
                return StyleBuilder(new_style_list)
            self._style_list.append(_styles[attr])
            return self
        raise AttributeError('%r object has no attribute %r' % (self.__class__.__name__, attr))
