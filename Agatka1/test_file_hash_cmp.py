import pytest
from file_hash_cmp import FileHashCmp


def test_compare_include():
    cmp = FileHashCmp()

    cmp.compare_include(["0"], ["a\\b.txt"], ["0", "1"], ["a\\b.txt", "a\\c.txt"])
    with pytest.raises(Exception) as pex:
        cmp.compare_include(["0", "1"], ["a\\b.txt", "a\\c.txt"], ["0"], ["a\\b.txt"])
    assert "missing hash 1 for file a\\c.txt" in str(pex.value)

    with pytest.raises(Exception) as pex:
        cmp.compare_include(["0", "B", "1"], ["a\\b.txt", "dd", "a\\c.txt"], ["0", "1"], ["a\\b.txt", "a\\c.txt"])
    assert "missing hash B for file dd" in str(pex.value)

def test_compare_include_by_filenames():
    cmp = FileHashCmp()
    with pytest.raises(Exception) as pex:
        cmp.compare_include(["0"], ["a\\c.txt"], ["0"], ["c\\b.txt"])
    assert "diff filenames for hash 0, filenames: a\\c.txt, c\\b.txt" in str(pex.value)

def test_compare_include_by_filenames2():
    cmp = FileHashCmp()
    cmp.compare_include(["0", "0"], ["a\\c.txt", "h\\c.txt"], ["0"], ["c\\c.txt"])
    with pytest.raises(Exception) as pex:
        cmp.compare_include(["0", "0"], ["a\\c.txt", "a\\d.txt"], ["0"], ["c\\c.txt"])
    assert "diff filenames for hash 0, filenames: a\\c.txt, a\\d.txt" in str(pex.value)
