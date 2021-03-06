# -*- coding: utf-8 -*-

"""
Tests for ipaddr generator
"""

from fauxfactory import FauxFactory

import unittest


class TestIpaddr(unittest.TestCase):
    """
    Test ipaddr generator
    """

    @classmethod
    def setUpClass(cls):
        """
        Instantiate our factory object
        """

        cls.factory = FauxFactory()

    def test_generate_ipv4_1(self):
        """
        @Test: Generate a 3 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 3-group IPv4 address is generated (addr
                 will always end with a \'.0\')
        """

        result = self.factory.generate_ipaddr(ip3=True)
        self.assertTrue(
            result.split(".")[-1] == '0',
            "Did not generate a 3-group IPv4 addrss")

    def test_generate_ipv4_2(self):
        """
        @Test: Generate a 4 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = self.factory.generate_ipaddr()
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")

    def test_generate_ipv4_3(self):
        """
        @Test: Generate a 4 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = self.factory.generate_ipaddr(ip3=False)
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")

    def test_generate_ipv4_4(self):
        """
        @Test: Generate a 4 group IPv4 address
        @Feature: IPAddr Generator
        @Assert: A 4-group IPv4 address is generated
        """

        result = self.factory.generate_ipaddr(ip3=False, ipv6=False)
        self.assertTrue(
            len(result.split(".")) == 4,
            "Did not generate a 4-group IPv4 addrss")

    def test_generate_ipv6_1(self):
        """
        @Test: Generate a IPv6 address
        @Feature: IPAddr Generator
        @Assert: A IPv6 address is generated
        """

        result = self.factory.generate_ipaddr(ipv6=True)
        self.assertTrue(
            len(result.split(":")) == 8,
            "Did not generate a IPv6 addrss")

    def test_generate_ipv6_2(self):
        """
        @Test: Generate a IPv6 address
        @Feature: IPAddr Generator
        @Assert: A IPv6 address is generated
        """

        result = self.factory.generate_ipaddr(ip3=True, ipv6=True)
        self.assertTrue(
            len(result.split(":")) == 8,
            "Did not generate a IPv6 addrss")
