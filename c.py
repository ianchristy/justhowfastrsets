
def allzeros(s) :
    s0 = s[0]
    return all(c == s0 for c in s[1:])

def test(v_str):
    if allzeros(v_str):
        print('  ALL ZEROS')
    else:
        print('   mix')


for k in range(1, 10000):
    test('00000000000000000000000000003030000000')
    test('00000000000000000000000000000000000000')
    test('00000000000000000000000000000000000001')
