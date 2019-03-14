from file_hash_cmp import FileHashCmp
from files_iter import FilesIter

if __name__ == '__main__':

    # iter_local = FilesIter()
    # # iter_local.scan_dir("C:\\Users\\jskoczyl\\Documents\\irving_imgs")
    # iter_local.scan_dir("F:\\copy_12.11.2017\\irving_2017_zrzuty")
    # print("hashing")
    # iter_local.make_hashes(8)
    # print("saving")
    # iter_local.save_to_file("remote_dict_db.pickle")
    # # with open("local_dict_db.pickle", 'wb') as f:
    # #     pickle.dump(iter_local.hash_to_abs_filename, f)
    # print("done all ok for local")
    # # return local_iter_thread, iter_local

    print("comparing pickle local and remote")
    iter_local = FilesIter("local_dict_db.pickle")
    iter_remote = FilesIter("remote_dict_db.pickle")
    cmp = FileHashCmp()
    cmp.compare_include(iter_local.hashes, iter_local.filenames, iter_remote.hashes, iter_remote.filenames)
    print("all ok")
