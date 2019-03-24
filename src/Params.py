class Params:

    def __init__(self, path_in):
        self.points = None
        self.paths = dict()

        self.__path_in = path_in
        self.__set()

    def __set(self):
        with open(self.__path_in, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.points = lines[0].strip().split(',')
            path_rows_number = int(lines[1].strip())
            path_lines = lines[2:]
            path_lines_number = len(path_lines)

            if path_lines_number < path_rows_number:
                msg = 'Expected `{}` rows with paths. Found `{}`!'.format(path_rows_number, path_lines_number)
                raise IOError(msg)

            for line in path_lines[:path_lines_number+1]:
                _from, _to, weight = line.strip().split(',')
                weight = float(weight.replace(',', '.'))
                if _from not in self.paths:
                    self.paths[_from] = dict()
                self.paths[_from][_to] = weight
