from src.Counter import Counter


def test_count_1():
    points = ['a', 'b']
    paths = {
        'a': {
            'b': 1
        }
    }
    expected = (['a', 'b'], 1)

    counter = Counter(points, paths, 1)
    actual = counter.count()
    assert actual == expected


def test_count_2():
    points = ['a', 'b']
    paths = {
        'a': {
            'b': 1
        },
        'b': {
            'a': 1
        }
    }
    expected = (['a', 'b', 'a'], 2)

    counter = Counter(points, paths, 1, True)
    actual = counter.count()
    assert actual == expected


def test_count_3():
    points = ['a', 'b']
    paths = {
        'a': {
            'b': 1,
            'a': 0,
        },
        'b': {
            'a': 1,
            'b': 0
        }
    }
    expected = (['a', 'b'], 1)

    counter = Counter(points, paths, 1)
    actual = counter.count()
    assert actual == expected


def test_count_4():
    points = ['a', 'b']
    paths = {
        'a': {
            'b': 1,
            'a': 0,
        },
        'b': {
            'a': 1,
            'b': 0
        }
    }
    expected = (['a', 'b', 'a'], 2)

    counter = Counter(points, paths, 1, True)
    actual = counter.count()
    assert actual == expected


def test_count_5():
    points = ['a', 'c']
    paths = {
        'a': {
            'b': 1,
            'a': 0,
            'c': 10,
        },
        'b': {
            'a': 1,
            'b': 0,
            'c': 2
        }
    }
    expected = (['a', 'b', 'c'], 3)

    counter = Counter(points, paths, 1)
    actual = counter.count()
    assert actual == expected


def test_count_6():
    points = ['a', 'c']
    paths = {
        'a': {
            'b': 1,
            'a': 0,
            'c': 10,
        },
        'b': {
            'a': 1,
            'b': 0,
            'c': 2
        },
        'c': {
            'a': 2,
            'b': 10,
            'c': 0
        }
    }
    expected = (['a', 'b', 'c', 'a'], 5)

    counter = Counter(points, paths, 1, True)
    actual = counter.count()
    assert actual == expected


def test_count_no_1():
    points = ['a', 'c']
    paths = {}
    expected = None

    counter = Counter(points, paths, 1)
    actual = counter.count()
    assert actual == expected


def test_count_no_2():
    points = ['a', 'c']
    paths = {}
    expected = None

    counter = Counter(points, paths, 1, True)
    actual = counter.count()
    assert actual == expected


def test_count_no_3():
    points = ['a', 'c']
    paths = {
        'a': {
            'b': 1
        },
        'b': {
            'a': 1
        }
    }
    expected = None

    counter = Counter(points, paths, 1)
    actual = counter.count()
    assert actual == expected


def test_count_no_4():
    points = ['a', 'c']
    paths = {
        'a': {
            'b': 1
        },
        'b': {
            'a': 1
        }
    }
    expected = None

    counter = Counter(points, paths, 1, True)
    actual = counter.count()
    assert actual == expected


def test_count_no_5():
    points = ['a', 'c']
    paths = {
        'a': {
            'b': 1
        },
        'b': {
            'a': 1,
            'c': 2
        }
    }
    expected = None

    counter = Counter(points, paths, 1, True)
    actual = counter.count()
    assert actual == expected


def test_count_no_6():
    points = ['a', 'c']
    paths = {
        'a': {
            'b': 1
        },
        'b': {
            'c': 2
        },
        'c': {
            'b': 1
        }
    }
    expected = None

    counter = Counter(points, paths, 1, True)
    actual = counter.count()
    assert actual == expected
