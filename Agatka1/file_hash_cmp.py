
class FileHashCmp(object):

    def __init__(self):
        pass

    def compare_include(self, a_hashes, a_filenames, b_hashes, b_filenames):
        a_only_hashes = set(a_hashes) - set(b_hashes)
        if len(a_only_hashes) != 0:
            self._raise_not_file_in_a(a_filenames, a_hashes, a_only_hashes)
        hash_to_filename = {}
        self._fill_hashes(a_filenames, a_hashes, hash_to_filename)
        self._fill_hashes(b_filenames, b_hashes, hash_to_filename)

    def _fill_hashes(self, a_filenames, a_hashes, hash_to_filename):
        for h, f in zip(a_hashes, a_filenames):
            # if h == "69eee7989c7bc067b697939339aacf99":
            #     continue
            if h in hash_to_filename:
                if self._to_filename(hash_to_filename[h]) != self._to_filename(f):
                    msg = f"diff filenames for hash {h}, filenames: {hash_to_filename[h]}, {f}"
                    # raise Exception(msg)
                    print(msg)
            hash_to_filename[h] = f

    def _to_filename(self, full_path_filename):
        return full_path_filename.split("\\")[-1]

    def _raise_not_file_in_a(self, a_filenames, a_hashes, a_only_hashes):
        missing_hash = a_only_hashes.pop()
        missing_filenames = [filename for h, filename in zip(a_hashes, a_filenames) if h == missing_hash]
        raise Exception(f"missing hash {missing_hash} for file {', '.join(missing_filenames)}")