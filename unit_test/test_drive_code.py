import unittest
from googl_drive_code.drive_code import DriveAPI


class DriveCodeTest(unittest.TestCase):
    """ Test class for drive code """
    def setUp(self):
        pass

    def test_for_execl(self):
        drive_api = DriveAPI().FileDownload('Enter execl file ID','xlsx namewith extension')
        self.assertEqual(drive_api, True)

    def test_for_image(self):
        drive_api = DriveAPI().FileDownload('Enter image file ID','Image name extension')
        self.assertEqual(drive_api, True)


