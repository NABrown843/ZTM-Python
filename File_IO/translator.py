from translate import Translator

translator = Translator(to_lang='ja')

with open('files\\translation_test.txt', mode='r') as my_file:
	txt = my_file.readline()

translation = translator.translate(txt)

with open('files\\test-ja.txt', mode='w') as my_file2:
	my_file2.write(translation)