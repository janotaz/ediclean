"""
Test: header removal
"""
import os
import unittest
import ediclean.paxlst as paxlst


class TestEdifact(unittest.TestCase):
    def test_files(self):
        testfiles_dir = os.path.join(os.path.dirname(__file__), "testfiles",
                                     "original")

        for root, dirs, files in os.walk(testfiles_dir):
            for file in sorted(files):

                basename = os.path.basename(file)

                # retrieve and clean original file
                with open(os.path.join(root, file), 'r') as file:
                    cleaned_file = paxlst.cleanfile(os.path.abspath(file.name))


# Write cleansed file to disk; for testing purposes
#                cleaned_file_dir = os.path.join(os.path.dirname(__file__), "testfiles", "cleaned")
#                if not os.path.exists(cleaned_file_dir):
#                    os.makedirs(cleaned_file_dir)
#
#                cleaned_file_pointer = open(os.path.join(os.path.dirname(__file__),
#                "testfiles", "cleaned", basename), "w")
#
#                #write string to file
#                n = cleaned_file_pointer.write(cleaned_file)
#
#                #close file
#                cleaned_file_pointer.close()

# read reference file
                with open(
                        os.path.join(os.path.dirname(__file__), "testfiles",
                                     "reference", basename), 'r') as ref_file:
                    reference_file = ref_file.read()

                # compare the cleaned file with the reference file
                self.assertEqual.__self__.maxDiff = None
                self.assertEqual(cleaned_file, reference_file)

if __name__ == '__main__':
    unittest.main()
