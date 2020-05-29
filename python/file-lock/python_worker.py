import fcntl
import os
import time


class LockDemo(object):
    def __init__(self):
        self.host_name = os.environ.get("HOSTNAME")
        self._lock_file = None

    def acquire_lock(self):
        print("[name {}][acquire_lock]acquiring lock...".format(self.host_name))
        if self._lock_file is None:
            self._lock_file = open("/app/lock.file.log", "a+")
        _time_start = time.time()
        fcntl.flock(self._lock_file.fileno(), fcntl.LOCK_EX)
        print("[name {}][acquire_lock] waited {:.3f} seconds".format(self.host_name, time.time() - _time_start))

    def release_lock(self):
        try:
            if self._lock_file:
                self._lock_file.close()
                self._lock_file = None
        except Exception as e:
            print("[name {}][release_lock]error is {}".format(self.host_name, e))

        print("[name {}][release_lock] success to release lock".format(self.host_name))

    def run(self):
        """ """
        while True:
            self.acquire_lock()
            time.sleep(1)
            print("[name {}]doing sth...".format(self.host_name))
            self.release_lock()


if __name__ == '__main__':
    LockDemo().run()
