# -*- coding: utf-8 -*-

"""
Tests for all boolean generators
"""

from fauxfactory import FauxFactory

import unittest


class TestBooleans(unittest.TestCase):
    """
    Test boolean generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_boolean_1(self):
        """Create a random boolean value"""

        for turn in xrange(100):
            result = self.factory.generate_boolean()
            self.assertTrue(
                isinstance(result, bool),
                "A valid boolean value was not generated.")