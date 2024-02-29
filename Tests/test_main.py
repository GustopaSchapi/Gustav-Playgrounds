import pytest


def test_dummy():
    with pytest.raises(SystemExit):
        raise SystemExit(1)
