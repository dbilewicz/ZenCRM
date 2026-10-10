import unittest


class MergeGateTest(unittest.TestCase):
    def test_deliberate_failure(self):
        self.fail("Temporary: verifies that a failing required check blocks merging")
