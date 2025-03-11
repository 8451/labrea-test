import pytest
import labrea_test
from labrea import Option


def test_mock():
    A = Option("A")

    with labrea_test.Mock() as mock:
        mock(A, 1)
        assert A() == 1
        A.validate({})
        assert A.keys({}) == set()
        assert A.explain() == set()

        mock(A, Option("B"))
        assert A({"B": 2}) == 2
        A.validate({"B": 2})
        assert A.keys({"B": 2}) == {"B"}
        assert A.explain() == {"B"}

    assert A({"A": 1}) == 1
    A.validate({"A": 1})
    assert A.keys({"A": 1}) == {"A"}
    assert A.explain() == {"A"}


def test_double_enter():
    with pytest.raises(RuntimeError):
        with labrea_test.Mock() as mock:
            with mock:
                pass


def test_double_exit():
    with pytest.raises(RuntimeError):
        with labrea_test.Mock() as mock:
            pass

        mock.__exit__(None, None, None)
