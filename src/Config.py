import configparser


class Config:

    def __init__(self, path_config, path_abs, path_in=None):
        cp = self.__cp(path_config)
        self.path_in = '{}/{}'.format(path_abs, path_in if path_in else cp.get('path', 'in'))
        self.path_out = '{}/{}'.format(path_abs, cp.get('path', 'out'))
        self.processes_number = int(cp.get('processes', 'number'))

    @staticmethod
    def __cp(path):
        cp = configparser.ConfigParser()
        cp.read(path)
        return cp
