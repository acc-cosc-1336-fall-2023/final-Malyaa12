#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_tests

suite = unittest.TestLoader().loadTestsFromModule(question_tests)
unittest.TextTestRunner(verbosity=2).run(suite)
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("tests")
    runner = unittest.TextTestRunner()
    runner.run(suite)
