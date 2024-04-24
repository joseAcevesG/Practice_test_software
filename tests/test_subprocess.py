import unittest
from unittest import mock
import subprocess

from src.subprocess import execute_command

class TestExecuteCommand(unittest.TestCase):
    @mock.patch('subprocess.run')
    def test_execute_command_success(self, mock_run):
        # Mock the subprocess.run function to return a successful result
        mock_run.return_value = subprocess.CompletedProcess(args=['ls'], returncode=0, stdout='file1.txt\nfile2.txt\n')

        # Call the function under test
        result = execute_command(['ls'])

        # Assert the expected result
        self.assertEqual(result, 'file1.txt\nfile2.txt\n')

    @mock.patch('subprocess.run')
    def test_execute_command_failure(self, mock_run):
        # Mock the subprocess.run function to raise a CalledProcessError
        mock_run.side_effect = subprocess.CalledProcessError(returncode=1, cmd=['ls'], output='')

        # Call the function under test and assert that it raises a CalledProcessError
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(['ls'])

if __name__ == '__main__':
    unittest.main()
