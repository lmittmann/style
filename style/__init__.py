import sys

from style.style_builder import _StyleBuilder


__version__ = '1.0.4'

_enabled = sys.stdout.isatty()
if '--color' in sys.argv:
    _enabled = True
elif '--no-color' in sys.argv:
    _enabled = False

style_builder = _StyleBuilder([], True)
style_builder.enabled = _enabled
style_builder.__version__ = __version__
sys.modules[__name__] = style_builder
