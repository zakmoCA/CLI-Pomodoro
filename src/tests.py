import unittest
from unittest.mock import patch, mock_open
from pomodoro_length import Pomodoro
from start_pomodoro import StartPomodoro
from run_pomodoro import Timer


class TestPomodoroApp(unittest.TestCase):

    # this test that my pomodoro_length function correctly handles user input
    def test_pomodoro_length(self):
        pomodoro = Pomodoro()

        with patch('builtins.input', side_effect=['4', '25', '5', '15']):
            cycle_length, work_time, short_break, long_break = pomodoro.user_preferences()
            self.assertEqual(cycle_length, 4)
            self.assertEqual(work_time, 25)
            self.assertEqual(short_break, 5)
            self.assertEqual(long_break, 15)
    """"
    My second test checks that my start funciton correctly writes something to csv.
    I can't check the exact timestamps are 'corect' because assert_called_once_with doesn't support regex
    But I am happy in checking that;
      > the headers and pomodoro are written correctly
      > the string that the write method is called with starts with the task name, and has the structure we expect
    """
    @patch('start_pomodoro.Timer.run_pomodoro')
    @patch('builtins.input')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.isfile')
    def test_write_pomodoro_to_csv(self, isfile_mock, mock_open, input_mock, run_pomodoro_mock):
        # define the behavior of the mocks
        input_mock.side_effect = ['test_task', '4', '25', '5', '15']
        run_pomodoro_mock.return_value = None
        isfile_mock.return_value = False  # mock isfile should return False,
        # this is to simulate a non-existent csv file, which is the case for the first pomodoro
        start_pomodoro = StartPomodoro()
        start_pomodoro.start()

        # get all calls to write
        write_calls = mock_open().write.call_args_list

        # the first call should be writing the headers
        call_args = write_calls[0][0][0]
        # check that first call writes headers
        # the OR statement is for checking newline characters in unix-based systems and windows
        self.assertTrue(call_args == 'Task Name,Start Time,End Time,Duration\n' or call_args ==
                        'Task Name,Start Time,End Time,Duration\r\n')

        # the second call should be writing the pomodoro
        call_args = write_calls[1][0][0]
        self.assertTrue(call_args.startswith('test_task,'))
        self.assertTrue(call_args.endswith('\n'))


if __name__ == '__main__':
    unittest.main()
