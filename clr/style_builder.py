import sys


_enabled = sys.stdout.isatty()
_styles = {
    'bold': 1,
    'bg_bold': 100,
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
    'bg_black': 40,
    'bg_red': 41,
    'bg_green': 42,
    'bg_yellow': 43,
    'bg_blue': 44,
    'bg_magenta': 45,
    'bg_cyan': 46,
    'bg_white': 47
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
            try:
                self._style_list.remove(_styles['bg_bold'])
                for i, val in enumerate(self._style_list):
                    if 40 <= val and val <= 47:
                        self._style_list[i] += 60
            except:
                pass
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
