from morse_chart import MorseConverter

conv = MorseConverter()

str_to_convert = input('Write some text: ')
print(conv.convert(str_to_convert))
