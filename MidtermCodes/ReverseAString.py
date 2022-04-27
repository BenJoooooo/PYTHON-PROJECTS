def reverseStr(S):
    result = ""
    for i in S:
        result = i + result
    return result

S = input('Input: ')
print(f'String: {S}')
print('Reversed:', reverseStr(S).upper(),len(reverseStr(S)), 'characters')