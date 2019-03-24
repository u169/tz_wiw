import os

from src.Config import Config


real_path_absolute = os.path.dirname(os.path.abspath(__file__))


def test__with_args():
    abs_path = '/app'
    path_in = 'input_file_name'
    path_out = 'out_file_name'
    processes_number = 8
    c = Config(abs_path, None, path_in, path_out, processes_number)

    assert c.path_in == '/app/input_file_name'
    assert c.path_out == '/app/out_file_name'
    assert c.processes_number == 8


def test__from_file():
    path_config = 'files/config/config.ini'

    abs_path = real_path_absolute
    c = Config(abs_path, path_config)

    assert c.path_in == '{}/in_file_name'.format(real_path_absolute)
    assert c.path_out == '{}/out_file_name'.format(real_path_absolute)
    assert c.processes_number == 16
