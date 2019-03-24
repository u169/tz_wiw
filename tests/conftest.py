import os


real_path_absolute = os.path.dirname(os.path.abspath(__file__))


def pytest_configure(config):
    storage_dir = '{}/files/result'.format(real_path_absolute)

    if not os.path.exists(storage_dir):
        os.mkdir(storage_dir)