




# python imports
import unittest, os, sys, shutil

# keepnote imports
from keepnote import notebook, safefile
import keepnote.notebook.connection as connlib


def clean_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


class Conn (unittest.TestCase):

    def test_basename(self):

        """
        Return the last component of a filename

        aaa/bbb   =>  bbb
        aaa/bbb/  =>  bbb
        aaa/      =>  aaa
        aaa       =>  aaa
        ''        =>  ''
        /         =>  ''
        """

        self.assertEqual(connlib.path_basename("aaa/b/ccc"), "ccc")
        self.assertEqual(connlib.path_basename("aaa/b/ccc/"), "ccc")
        self.assertEqual(connlib.path_basename("aaa/bbb"), "bbb")
        self.assertEqual(connlib.path_basename("aaa/bbb/"), "bbb")
        self.assertEqual(connlib.path_basename("aaa"), "aaa")
        self.assertEqual(connlib.path_basename("aaa/"), "aaa")
        self.assertEqual(connlib.path_basename(""), "")
        self.assertEqual(connlib.path_basename("/"), "")


        
if __name__ == "__main__":
    unittest.main()
