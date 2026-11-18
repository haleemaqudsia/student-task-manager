import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Python")
        self.assertEqual(task["title"], "Study Python")
        self.assertEqual(len(self.manager.display_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Study Python")
        self.assertTrue(self.manager.complete_task(task["id"]))
        self.assertTrue(task["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Study Python")
        self.assertTrue(self.manager.delete_task(task["id"]))
        self.assertEqual(self.manager.display_tasks(), [])

