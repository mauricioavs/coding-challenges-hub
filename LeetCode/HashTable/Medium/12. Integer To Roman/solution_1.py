class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        value = [1000, 500, 100, 50, 10, 5, 1]
        remainder = num
        result = ''
        last_sym = None
        for sym, val in zip(symbol, value):
            quotient = remainder // val
            if result != '':
                last_sym = result[-1]

            if quotient == 4 and sym == 'I':
                match last_sym:
                    case 'V':
                        result = result[:-1] + 'IX'
                    case default:
                        result += 'IV'

            elif quotient == 4 and sym == 'X':
                match last_sym:
                    case 'L':
                        result = result[:-1] + 'XC'
                    case default:
                        result += 'XL'

            elif quotient == 4 and sym == 'C':
                match last_sym:
                    case 'D':
                        result = result[:-1] + 'CM'
                    case default:
                        result += 'CD'

            elif quotient > 0:
                result += sym * quotient
            remainder -= quotient * val

        return result