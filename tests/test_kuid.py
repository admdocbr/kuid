import uuid
import unittest
from kuid import encode, decode, kuid1, kuid3, kuid4, kuid5


class TestKuid(unittest.TestCase):
    def test_encode_decode(self):
        u = uuid.uuid4()
        assert decode(encode(u)) == u

    def test_kuid1(self):
        assert isinstance(decode(kuid1()), uuid.UUID)

    def test_kuid3(self):
        assert isinstance(decode(kuid3(namespace=uuid.uuid4(), name="foo")), uuid.UUID)

    def test_kuid4(self):
        assert isinstance(decode(kuid4()), uuid.UUID)

    def test_kuid5(self):
        assert isinstance(decode(kuid5(namespace=uuid.uuid4(), name="foo")), uuid.UUID)


if __name__ == "__main__":
    unittest.main()
