import sys

from style.style_builder import _StyleBuilder


_enabled = sys.stdout.isatty()
if '--color' in sys.argv:
    _enabled = True
elif '--no-color' in sys.argv:
    _enabled = False

style_builder = _StyleBuilder([], True)
style_builder.enabled = _enabled
sys.modules[__name__] = style_builder
