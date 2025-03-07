# Usage

During testing, you may want to mock a certain dataset (or other `Evaluatable`) to known value.
This can be done using the `labrea_test.Mock` context manager, which ensures that at the end
of the block, any mocking is torn down.

```python
import labrea_test
from labrea import dataset


@dataset
def foo() -> str:
    return "foo"


def test_foo():
    with labrea_test.Mock() as mock:
        mock(foo, "bar")
        assert foo() == "bar"

    assert foo() == "foo"
```

`Mock` can be used to mock any `Evaluatable` object, and can take a plain value or another
`Evaluatable` object as the value to mock to.

```python
import labrea_test
from labrea import dataset


@dataset
def foo() -> str:
    return "foo"


@dataset
def bar() -> str:
    return "bar"


def test_foo():
    with labrea_test.Mock() as mock:
        mock(foo, bar)
        assert foo() == "bar"

    assert foo() == "foo"
```
