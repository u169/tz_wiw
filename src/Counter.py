from multiprocessing import Pool


class Counter:

    def __init__(self, points, paths, process_num, need_back=False):
        self.__points = points
        self.__paths = paths
        self.__process_num = process_num

        if need_back:
            self.__points.append(points[0])

    def count(self):
        pool = Pool(self.__process_num)
        pool_result = pool.map(Task.shorter, self.__task_args())

        ways = [x[0] for x in pool_result]
        if not all(ways):
            return None
        way = list(ways[0])
        for w in ways[1:]:
            way.extend(w[1:])

        way_len = sum(x[1] for x in pool_result)

        return way, way_len

    def __task_args(self):
        start_point = self.__points[0]

        for finish_point in self.__points[1:]:
            yield start_point, finish_point, self.__paths
            start_point = finish_point


class Task:

    @staticmethod
    def shorter(args):
        start_dot, finish_dot, paths = args
        all_ways = Task.__ways(paths, start_dot, finish_dot, [], set())

        if not all_ways:
            way, s = None, None
        else:
            all_ways_len = list(map(lambda x: Task.__way_len(x, paths), all_ways))
            shorter_index = all_ways_len.index(min(all_ways_len))
            shorter_way = all_ways[shorter_index]
            shorter_len = all_ways_len[shorter_index]
            way, s = shorter_way, shorter_len

        return way, s

    @staticmethod
    def __way_len(path, paths):
        res = 0

        a = path[0]
        for e in path[1:]:
            res += paths[a][e]
            a = e
        return res

    @staticmethod
    def __ways(paths, _from, _to, road, visited):
        results = list()

        visited.add(_from)

        if _from not in paths:
            return results

        available = list(filter(lambda x: x not in visited, paths[_from]))

        if _to in available:
            results += [road + [_from, _to]]

        list(map(
            lambda a: results.extend(Task.__ways(paths, a, _to, road + [_from], visited.copy())),
            available
        ))

        return results
