def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    diff = 5 - 3
    try:
        assert diff == 23, 'chucuo 了吗'
    except Exception as e:
        print(e.args)
# test_subtraction()
#在本地pycharm中，修改了本文件，0824日，18:17分