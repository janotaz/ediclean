"""
Test: clean entire directory of files
"""
import os
import unittest
import ediclean.paxlst as paxlst


class TestEdifact(unittest.TestCase):
    """ This test only checks if the cleandir command cleaned all files in the folder
        by determining their existence and verifying if the file content is EDIFACT
    """
    def test_header(self):

        # this test only checks if the cleandir command cleaned all files in the folder
        # by determining their existence and verifying if the file content is EDIFACT

        testfiles_dir = os.path.join(os.path.dirname(__file__), "testfiles",
                                     "original")

        target_dir = os.path.join(os.path.dirname(__file__), "testfiles",
                                     "cleandir")

        # create target dir if it does not exist
        try:
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
        except OSError:
            print ("Creation of the directory %s failed" % target_dir)
        else:
            print ("Successfully created the directory %s " % target_dir)


        paxlst.cleandir(testfiles_dir, target_dir)

        # for every cleaned file, check if it is valid PAXLST
        self.assertEqual.__self__.maxDiff = None
        for root, dirs, files in os.walk(target_dir):
            for file in sorted(files):
                with open(os.path.join(root, file), 'r') as file:
                    filecontent = file.read()

                    self.assertTrue(paxlst.is_paxlst(filecontent))


if __name__ == '__main__':
    unittest.main()
