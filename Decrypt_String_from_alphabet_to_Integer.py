# def freqAlphabets( s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     d = dict()
#     alphabets = "abcdefghijklmnopqrstuvwxyz"
#     for index, letter in enumerate(alphabets):
#         d[str(index + 1)] = letter
#
#
#
#     ans = ''
#     numbers = s.split('#')
#     if s[-1] == '':
#         numbers.remove('')
#
#     for number in numbers[:-1]:
#
#         if len(number) > 2 :
#             double_no = number[-2:]
#             singles = number[:-2]
#
#             for i in singles:
#                 ans += d[i]
#
#             ans += d[double_no]
#         else:
#             ans += d[number]
#
#     if s[-1] != '#':
#         for i in numbers[-1]:
#             ans += d[i]
#     else:
#         ans += d[s[-1]]
#     return ans
#
#
#
#
# # print(freqAlphabets('1326#'))
# print("1326#".split('#'))

def freqAlphabets( s):
    """
    :type s: str
    :rtype: str
    """
    d = dict()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for index, letter in enumerate(alphabets):
        d[str(index + 1)] = letter

    numbers = s.split("#")
    ans = ""

    #Two cases
    if s[-1] == '#':
        numbers.remove('')
        for number in numbers:
            if len(number) > 2:
                double = number[-2:]
                single = number[:-2]

                for i in single:
                    ans += d[i]
                ans += d[double]
            else:
                ans += d[number]
        return ans
    else:
        for number in numbers[:-1]:
            if len(number) >2:
                double = number[-2:]
                single = number[:-2]

                for i in single:
                    ans += d[i]
                ans += d[double]
            else:
                ans += d[number]

        for digit in numbers[-1]:
            ans += d[digit]
        return ans

print(freqAlphabets('1326#'))

