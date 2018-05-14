import core
import pytest

def test_threads_lite():
    # valid board
    data = core.get_threads_lite("b")
    assert data["board"] == "b"
    assert len(data["threads"]) > 0

    # invalid board specified
    data = core.get_threads_lite("perkele")
    assert not data

def test_thread_list():
    # page not stated; using the default value (0)
    data = core.get_thread_list("b")
    assert data["Board"] == "b"
    assert len(data["threads"]) > 0

    # page stated explicitly
    data = core.get_thread_list("b", 1)
    assert data["Board"] == "b"
    assert len(data["threads"]) > 0

    # page out of range
    data = core.get_thread_list("b", 42)
    assert not data