import argparse
import os

from src.Config import Config
from src.Counter import Counter
from src.Params import Params
from src.Result import Result

path_absolute = os.path.dirname(os.path.abspath(__file__))
config_path = '{}/src/config.ini'.format(path_absolute)


def arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path_in', type=str, nargs='?',
                        help='path to test.in')

    result = parser.parse_args()
    return result


def main():
    args = arguments()
    config = Config(config_path, path_absolute, args.path_in)
    params = Params(config.path_in)
    counter = Counter(params.points, params.paths, config.processes_number)
    counter_result = counter.count()
    result = Result(config.path_out, counter_result)
    result.save()


if __name__ == '__main__':
    main()
