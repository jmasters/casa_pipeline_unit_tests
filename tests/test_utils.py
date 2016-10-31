import os
import uuid  # used to generate unique non-existent filename
import unittest
import pipeline.infrastructure.utils as utils

data_path = os.environ.get('CASAPATH').split()[0] + 'data/regression/exportasdm/input'

if 'TEST_DATADIR' in os.environ:
    DATADIR = str(os.environ.get('TEST_DATADIR')) + '/utils/'
    if os.path.isdir(DATADIR):
        data_path = DATADIR
    else:
        print('WARN: directory {} does not exist.'.format(DATADIR))

print('utils tests will use data from {}'.format(data_path))


class CheckPpr(unittest.TestCase):
    def test_check_valid(self):
        self.assertTrue(utils.check_ppr(data_path + "PPR_valid_VLAT003.xml"))

    def test_check_undefined_task(self):
        self.assertFalse(utils.check_ppr(data_path + "PPR_invalid_VLAT003.xml"))

    def test_check_empty(self):
        self.assertFalse(utils.check_ppr(data_path + "PPR_empty.xml"))

    def test_check_nonexistent_file(self):
        self.assertFalse(utils.check_ppr(str(uuid.uuid4())))


def suite():
    return [CheckPpr]

