import requests
import eventlet

def threads_lite(board):
    return "https://2ch.hk/{0}/threads.json".format(board)

def get_threads_lite(board):
    timeout = eventlet.Timeout(10)
    try:
        data = requests.get(threads_lite(board))
        return data.json()
    except eventlet.timeout.Timeout:
        return None
    except ValueError:  # invalid request/404
        return None
    finally:
        timeout.cancel()

def thread_list(board, page = 0):
    if page is 0:
        page = "index"
    return "https://2ch.hk/{0}/{1}.json".format(board, page)

def get_thread_list(board, page = 0):
    timeout = eventlet.Timeout(10)
    try:
        data = requests.get(thread_list(board, page))
        return data.json()
    except eventlet.timeout.Timeout:
        return None
    except ValueError:  # invalid request/404
        return None
    finally:
        timeout.cancel()