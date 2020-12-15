#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest
import platform

sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import OrderedDict

dict = OrderedDict

from wine_get_version import wine_get_version


class Tests(unittest.TestCase):

	def testSimple(self):
		if platform.system() == "Windows":
			wine_get_version()
		else:
			self.assertEqual(wine_get_version(), None)


if __name__ == "__main__":
	unittest.main()
