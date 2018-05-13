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
    finally:
        timeout.cancel()