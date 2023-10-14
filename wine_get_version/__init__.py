import typing
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-libs/wine_get_version.py , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

__all__ = ("wine_get_version",)

try:
	from ctypes import c_char_p, windll

	_wine_get_version = windll.ntdll.wine_get_version
except Exception as ex:
	def wine_get_version() -> typing.Optional[str]:
		return None

else:
	_wine_get_version.argtypes = []
	_wine_get_version.restype = c_char_p

	def wine_get_version() -> typing.Optional[str]:
		return _wine_get_version().decode("utf-8")
