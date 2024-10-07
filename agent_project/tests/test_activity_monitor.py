# tests/test_activity_monitor.py
import unittest
from src.activity_monitor import ActivityMonitor

class TestActivityMonitor(unittest.TestCase):
    def test_activity_monitor_initialization(self):
        monitor = ActivityMonitor()
        self.assertIsNotNone(monitor.last_activity_time)

    # Add more tests...

if __name__ == '__main__':
    unittest.main()
