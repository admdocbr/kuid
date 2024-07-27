import uuid
import unittest
from kuid import encode, decode


class TestKuid(unittest.TestCase):
    def test_encode_decode(self):
        u = uuid.uuid4()
        assert decode(encode(u)) == u


if __name__ == "__main__":
    unittest.main()
