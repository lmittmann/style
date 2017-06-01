import sys
import types

from style.ansi import _styles


_module_name = __name__.split('.')[0]


class _StyleBuilder(types.ModuleType):
    _enabled = True

    @property
    def enabled(self):
        return _StyleBuilder._enabled

    @enabled.setter
    def enabled(self, value):
        _StyleBuilder._enabled = value

    def __init__(self, style_list, is_root=False):
        super(_StyleBuilder, self).__init__(_module_name)
        self._style_list = style_list
        self._is_root = is_root

    def __call__(self, *objects, **kwargs):
        if self._is_root:
            raise TypeError('%r object is not callable' % self.__class__.__bases__[0].__name__)

        sep = kwargs.get('sep', ' ')
        if type(sep) is not str:
            raise TypeError('sep must be None or a string, not %r' % sep.__class__.__name__)

        string = sep.join(str(obj) for obj in objects)
        if self.enabled:
            return '\033[%sm%s\033[0m' % (';'.join([str(val) for val in self._style_list]), string)
        return string

    def __getattr__(self, attr):
        if attr in _styles:
            if self._is_root:
                new_style_list = self._style_list[:]
                new_style_list.append(_styles[attr][0])
                return _StyleBuilder(new_style_list)
            self._style_list.append(_styles[attr][0])
            return self
        raise AttributeError('%r object has no attribute %r' % (self.__class__.__name__, attr))
