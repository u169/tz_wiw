import configparser


class Config:

    def __init__(self, path_abs, path_config, path_in=None, path_out=None, process_number=0):
        path_config = '{}/{}'.format(path_abs, path_config)
        cp = self.__cp(path_config)
        self.path_in = '{}/{}'.format(path_abs, path_in if path_in else cp.get('path', 'in'))
        self.path_out = '{}/{}'.format(path_abs, path_out if path_out else cp.get('path', 'out'))
        self.processes_number = int(process_number if process_number else cp.get('processes', 'number'))

    @staticmethod
    def __cp(path):
        cp = configparser.ConfigParser()
        cp.read(path)
        return cp
