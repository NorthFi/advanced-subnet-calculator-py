# root/tests/test_usable_ipv4.py
import importlib.util
import ipaddress
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / "advanced-subnet-calculator.py"
spec = importlib.util.spec_from_file_location("advanced_subnet_calculator", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class UsableRangeTests(unittest.TestCase):
    def test_24(self):
        self.assertEqual(module.usable_ipv4_range(ipaddress.IPv4Network("192.0.2.0/24")), (ipaddress.IPv4Address("192.0.2.1"), ipaddress.IPv4Address("192.0.2.254"), 254))

    def test_31(self):
        self.assertEqual(module.usable_ipv4_range(ipaddress.IPv4Network("192.0.2.10/31")), (ipaddress.IPv4Address("192.0.2.10"), ipaddress.IPv4Address("192.0.2.11"), 2))

    def test_32(self):
        self.assertEqual(module.usable_ipv4_range(ipaddress.IPv4Network("192.0.2.10/32")), (ipaddress.IPv4Address("192.0.2.10"), ipaddress.IPv4Address("192.0.2.10"), 1))


if __name__ == "__main__":
    unittest.main()
