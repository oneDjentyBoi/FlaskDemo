import t

import pytest

@pytest.mark.parametrize(
        ('inp','out'),
        (
            (5,25),
            (3.,9.)
        )
)
def test_square(inp, out):
    assert t.square(inp) == out
