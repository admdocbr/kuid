import uuid
from kuid import encode, decode


def test_encode_decode():
    u = uuid.uuid4()
    assert decode(encode(u)) == u
