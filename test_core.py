import py2ch.core as core
import pytest
import webbrowser

def test_threads_lite():
    # valid board
    data = core.get_threads_lite("b")
    assert data["board"] == "b"
    assert len(data["threads"]) > 0

    # invalid board
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

    # invalid board
    data = core.get_thread_list("perkele")
    assert not data

def test_catalog():
    # valid board
    data = core.get_catalog("b")
    assert data["Board"] == "b"
    assert len(data["threads"]) > 0

    # invalid board
    data = core.get_catalog("perkele")
    assert not data

def test_catalog_num():
    # valid board
    data = core.get_catalog_num("b")
    assert data["Board"] == "b"
    assert len(data["threads"]) > 0

    # invalid board
    data = core.get_catalog_num("perkele")
    assert not data

def test_thread():
    # valid board and thread id
    data = core.get_threads_lite("b")
    id = data["threads"][0]["num"]
    thread = core.get_thread("b", id)
    assert thread["Board"] == "b"
    assert thread["current_thread"] == id

    # invalid board
    thread = core.get_thread("perkele", 1)
    assert not thread

    # invalid thread id
    thread = core.get_thread("b", 42)
    assert not thread

def test_captcha_id():
    captcha = core.get_captcha_id("b")
    assert len(captcha["id"]) == 64
    assert captcha["result"] == 1

def open_image(path):
    webbrowser.open_new(path)

def test_captcha_image():
    open_image(core.get_captcha_image(core.get_captcha_id("b")["id"]))
    assert True