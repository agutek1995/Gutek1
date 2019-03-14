import pickle
import os
import sys
import hashlib
from multiprocessing import Pool
import time
import subprocess
import threading
import traceback


def hash_file(abs_filename: str):
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()
    # sha1 = hashlib.sha1()
    try:

        with open(abs_filename, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
                # sha1.update(data)
    except PermissionError:
        print(f"PermissionError hash for {abs_filename}")

    return md5.hexdigest()
    # return sha1.hexdigest()

def hash_file2(abs_filename: str):
    result = subprocess.run(['fciv', abs_filename], stdout=subprocess.PIPE)
    text = str(result.stdout)
    return text.split('\\n')[-2].split(' ')[0]


class FilesIter(object):

    def __init__(self, pickle_filename=None):
        self.filenames = []
        self.hashes = []
        self.hash_to_abs_filename = None
        if pickle_filename is not None:
            with open(pickle_filename, 'rb') as f:
                to_load = pickle.load(f)
                self.filenames = to_load["filenames"]
                self.hashes = to_load["hashes"]

    def scan_dir(self, dir_name: str):
        for filename in os.listdir(dir_name):
            abs_filename = os.path.join(dir_name, filename)
            if os.path.isdir(abs_filename):
                try:
                    self.scan_dir(abs_filename)
                except PermissionError:
                    print(f"PermissionError for {abs_filename}")
                continue
            if os.path.isfile(abs_filename):
                self.filenames.append(abs_filename)

    def make_hashes(self, pool_size):
        print("created dict:")
        p = Pool(pool_size)
        self.hashes = p.map(hash_file, self.filenames)
        # self.hash_to_abs_filename = dict(zip(hashes, self.filenames))

        # self.hash_to_abs_filename = {}
        # for hash, filename in zip(hashes, self.filenames):
        #     if hash in self.hash_to_abs_filename:
        #         msg = f"COLLISION HASH {hash}\n for files:\n{filename}\n and \n{self.hash_to_abs_filename[hash]}"
        #         print(msg)
        #         raise Exception(msg)
        #     self.hash_to_abs_filename[hash] = filename
        # return self.hash_to_abs_filename

    def save_to_file(self, filename="local_dict_db.pickle"):
        with open(filename, 'wb') as f:
            to_save = {"filenames": self.filenames, "hashes": self.hashes}
            pickle.dump(to_save, f)
        print(f"saved ok {len(self.hashes)} hashes to file {filename}")

    def scan_dir_in_thread(self, dir_name: str, pool_size: int):
        def _run():
            try:
                self.scan_dir(dir_name)
                self.make_hashes(pool_size)
                print(f"done succes for dir: {dir_name}")
            except Exception as ex:
                print(ex)
                traceback.print_exc()
        thread = threading.Thread(target=_run)
        thread.start()
        return thread

if __name__ == '__main__':

    iter_local = FilesIter()
    iter_local.scan_dir("C:\\Users\\jskoczyl\\Documents\\irving_imgs")
    print("hashing")
    iter_local.make_hashes(8)
    print("saving")
    iter_local.save_to_file()
    # with open("local_dict_db.pickle", 'wb') as f:
    #     pickle.dump(iter_local.hash_to_abs_filename, f)
    print("done all ok for local")
    # return local_iter_thread, iter_local

# if __name__ == '__main__':
# if __name__ == '__main__':
# if __name__ == '__main__':
# if __name__ == '__main__':
    # iter1 = FilesIter()
    # iter1.scan_dir("F:\\copy_26.02.2019\\C_Downloads")
    # iter1.make_hashes(20)
    # print(hash_file2('F:\\copy_26.02.2019\\C_Downloads\\cudowny chlopak.mp4'))
    iter_local = FilesIter()
    local_iter_thread = iter_local.scan_dir_in_thread("C:\\Users\\jskoczyl\\Documents\\irving_imgs", 8)