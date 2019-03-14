from file_hash_cmp import FileHashCmp
from files_iter import FilesIter

if __name__ == '__main__':
    iter_d = FilesIter("d_db.pickle")
    # iter_d.scan_dir("D:\\documents\\Documents\\Documents")
    # print("starting")
    # iter_d.make_hashes(8)
    # print("saving d")
    # iter_d.save_to_file("d_db.pickle")

    iter_c = FilesIter()
    iter_c.scan_dir("C:\\Users\\jskoczyl\\\Documents")
    iter_c.make_hashes(8)
    print("saving c")
    iter_c.save_to_file("c_db.pickle")

    # with open("local_dict_db.pickle", 'wb') as f:
    #     pickle.dump(iter_local.hash_to_abs_filename, f)
    print("done ok for local")
    # return local_iter_thread, iter_local

    print("comparing pickle local and remote")
    # iter_local = FilesIter("local_dict_db.pickle")
    # iter_remote = FilesIter("remote_dict_db.pickle")
    cmp = FileHashCmp()
    cmp.compare_include(iter_d.hashes, iter_d.filenames, iter_c.hashes, iter_c.filenames)
    print("all ok")
