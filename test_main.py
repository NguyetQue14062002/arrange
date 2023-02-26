import unittest
from main import sap_xep_tang_dan

class TestSapXepTangDan(unittest.TestCase):
    def test_sap_xep_tang_dan(self):
        # Gán giá trị cho mảng
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

        # Gọi hàm sắp xếp tăng dần và lưu kết quả vào biến result
        result = sap_xep_tang_dan(arr)

        # Kiểm tra kết quả
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])