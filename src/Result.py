class Result:

    def __init__(self, path_out, counter_result):
        self.__path_out = path_out

        self.__way, self.__way_len = counter_result if counter_result else (None, None)

        if self.__way_len:
            way_len_str = str(self.__way_len)
            before_dot, after_dot = way_len_str.split('.')
            after_dot_len = len(after_dot)
            if after_dot == '0' * after_dot_len:
                self.__way_len = int(before_dot)

    def save(self):
        with open(self.__path_out, 'w', encoding='utf-8') as file:
            to_write = '{}\n{}'.format(','.join(self.__way), self.__way_len) if self.__way else 'No'
            file.write(to_write)
