import argparse
import os

from src.Config import Config
from src.Counter import Counter
from src.Params import Params
from src.Result import Result


path_absolute = os.path.dirname(os.path.abspath(__file__))
path_config = '/src/config.ini'


def arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path_in', type=str, nargs='?',
                        help='path to test.in')
    parser.add_argument('path_out', type=str, nargs='?',
                        help='path to test.out')
    parser.add_argument('process_number', type=int, nargs='?',
                        help='available cores')

    result = parser.parse_args()
    return result


def main():
    args = arguments()
    config = Config(path_absolute, path_config, args.path_in, args.path_out, args.process_number)
    params = Params(config.path_in)
    counter = Counter(params.points, params.paths, config.processes_number)
    counter_result = counter.count()
    result = Result(config.path_out, counter_result)
    result.save()


if __name__ == '__main__':
    main()
