
from collections import Counter

def allzeros(s) :
    c = Counter(s)
    if len(c) == 1:
        return True

    return False


def test(v_str):
    if allzeros(v_str):
        print('  ALL ZEROS')
    else:
        print('   mix')


for k in range(1, 10000):
    test('00000000000000000000000000003030000000')
    test('00000000000000000000000000000000000000')
    test('00000000000000000000000000000000000001')
