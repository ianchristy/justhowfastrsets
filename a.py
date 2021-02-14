
def allzeros(s) :
    n = len(s)
    for i in range(1, n) :
        if s[i] != '0' :
            return False
    return True


def test(v_str):
    if allzeros(v_str):
        print('  ALL ZEROS')
    else:
        print('   mix')


for k in range(1, 10000):
    test('00000000000000000000000000003030000000')
    test('00000000000000000000000000000000000000')
    test('00000000000000000000000000000000000001')
