import core
import pytest

def test_threads_lite():
    data = core.get_threads_lite("b")
    assert data["board"] == "b"
    assert len(data["threads"]) > 0