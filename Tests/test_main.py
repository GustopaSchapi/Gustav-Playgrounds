import pytest
from Source.main import main


def test_main(capfd):
    main()
    out, err = capfd.readouterr()
    assert (lambda x: True if "\neeeeaaaa" in x else False)(out)
