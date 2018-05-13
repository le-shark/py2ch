import requests
import eventlet

def threads_list(board):
    return "https://2ch.hk/{0}/threads.json".format(board)

def get_threads(board)
    timeout = eventlet.Timeout(10)
    try:
        threads = requests.get(threads_list(board))
        return threads.json()
    except eventlet.timeout.Timeout:
        return None
    finally:
        timeout.cancel()