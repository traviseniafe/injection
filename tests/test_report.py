import json
import tempfile
import unittest
from pathlib import Path

from harness.report import write_report


class ReportTests(unittest.TestCase):
    def test_writes_json_report(self):
        evaluations = [{
            "attack_id": "direct-001",
            "category": "direct_override",
            "response": "I will keep it private.",
            "status": "no_leak_detected",
        }]

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "report.json"
            write_report(evaluations, str(path))
            saved_data = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(saved_data, evaluations)


if __name__ == "__main__":
    unittest.main()