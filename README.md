# Student Task Manager

Project status: In Development and Testing

A Python console app that adds, displays, completes, and deletes student tasks.
It rejects blank titles and handles invalid task IDs.

## Setup and usage

You need Python 3. No extra packages are required.

```bash
git clone https://github.com/haleemaqudsia/student-task-manager.git
cd student-task-manager
python main.py
```

Choose an option from the menu. Display your tasks to find their IDs before
completing or deleting them. See the [user guide](docs/user-guide.md).

## Run the tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the tests on pushes to `main` and pull requests targeting `main`.
