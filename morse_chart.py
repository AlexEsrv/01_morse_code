class MorseConverter:
    def __init__(self):
        self.morse_dict = {'A': '• −',
                        'B':'− • • •',
                        'C':'− • − •',
                        'D':'− • •',
                        'E':'•',
                        'F':'• • − •',
                        'G':'− − •',
                        'H':'• • • •',
                        'I':'• •',
                        'J':'• − − −',
                        'K':'− • −',
                        'L':'• − • •',
                        'M':'− −',
                        'N':'− •',
                        'O':'− − −',
                        'P':'• − − •',
                        'Q':'− − • −',
                        'R':'• − •',
                        'S':'• • •',
                        'T':'−',
                        'U':'• • −',
                        'V':'• • • −',
                        'W':'• − −',
                        'X':'− • • −',
                        'Y':'− • − −',
                        'Z':'− − • •',
                        '0':'− − − − −',
                        '1':'• − − − −',
                        '2':'• • − − −',
                        '3':'• • • − −',
                        '4':'• • • • −',
                        '5':'• • • • •',
                        '6':'− • • • •',
                        '7':'− − • • •',
                        '8':'− − − • •',
                        '9':'− − − − •'}

    def convert(self, str_to_convert):
        str_result = ''
        for char in str_to_convert:
            str_result += ' ' + self.morse_dict.get(char.upper()).replace(' ', '')
        return str_result
