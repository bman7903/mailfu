import seccure
import six

""" Tests for specific issues that were reported on Github.

    See https://github.com/bwesterb/py-seccure/issues """

import unittest

import gmpy

import seccure

class TestIssues(unittest.TestCase):
    def test_issue5(self):
        self.assertEqual(repr(seccure.passphrase_to_pubkey(b'my private key')),
                            '<PubKey 8W;>i^H0qi|J&$coR5MFpR*Vn>')


    def test_issue10(self):
        for curvename in seccure.curves:
            curve = seccure.Curve.by_name(curvename)
            for pt in (curve.base, curve.base * gmpy.mpz(1337)):
                self.assertEqual(pt + pt, pt * gmpy.mpz(2))

if __name__ == '__main__':
    unittest.main()