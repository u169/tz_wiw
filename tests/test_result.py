import os

from src.Result import Result


real_path_absolute = os.path.dirname(os.path.abspath(__file__))


def file_to_string(fp):
    with open(fp, 'r', encoding='utf-8') as file:
        result = ''.join(file.readlines())
        return result


def test__save_1():
    fp_out = '{}/files/result/test.out'.format(real_path_absolute)
    counter_result = (['a', 'b', 'c'], 10.0)

    expected = 'a,b,c\n10'

    result = Result(fp_out, counter_result)
    result.save()

    actual = file_to_string(fp_out)

    assert expected == actual

    os.remove(fp_out)


def test__save_2():
    fp_out = '{}/files/result/test.out'.format(real_path_absolute)
    counter_result = (None, None)

    expected = 'No'

    result = Result(fp_out, counter_result)
    result.save()

    actual = file_to_string(fp_out)

    assert expected == actual

    os.remove(fp_out)


def test__save_3():
    fp_out = '{}/files/result/test.out'.format(real_path_absolute)
    counter_result = (['a', 'b', 'c'], 10.1111)

    expected = 'a,b,c\n10.1111'

    result = Result(fp_out, counter_result)
    result.save()

    actual = file_to_string(fp_out)

    assert expected == actual

    os.remove(fp_out)
