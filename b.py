
# this logic just verifies they are all the same character
#def allzeros(s):
#    myset = set(s) 
#    if len(myset) == 1:
#        return True
#
#    return False

def allzeros(s):
    if len(s) > 0:
        myset = set(s) 
        if len(myset) == 1 and s[0] =='0':
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
