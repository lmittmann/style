import sys


_enabled = sys.stdout.isatty()
_styles = {
    'bold': 1,
    'bgBold': 100,
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
    'bgBlack': 40,
    'bgRed': 41,
    'bgGreen': 42,
    'bgYellow': 43,
    'bgBlue': 44,
    'bgMagenta': 45,
    'bgCyan': 46,
    'bgWhite': 47
}


class StyleBuilder:
    def __init__(self, style_list, is_root=False):
        self._style_list = style_list
        self._is_root = is_root

    def __call__(self, *strings):
        string = ' '.join(strings)
        if _enabled and self._style_list:
            try:
                self._style_list.remove(_styles['bgBold'])
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
