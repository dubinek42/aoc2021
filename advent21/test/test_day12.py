import pytest
from advent21.day12 import count_paths


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("day12_test.txt", (10, 36)),
        ("day12_test2.txt", (19, 103)),
        ("day12_test3.txt", (226, 3509)),
    ],
)
def test_count_paths(filename, expected):
    assert expected == count_paths(filename)
