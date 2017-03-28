import sys

from style.style_builder import StyleBuilder, _styles


__module__ = sys.modules[__name__]
for key, value in _styles.items():
    setattr(__module__, key, StyleBuilder([value], True))
