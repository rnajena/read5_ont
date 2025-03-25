try:
  from read5_ont._version import version as __version__
except ImportError:
  __version__ = "unknown"

from read5_ont.Reader import read

__all__ = [
    "read"
]