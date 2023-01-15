#Напишите программу, удаляющую из текста все слова, содержащие "абв".


text = 'Привет, меабв! ааааа вабв, ааа! Вабв, абв'
print(text)
print ('После удаления всех слов, содержащих абв: ')
data = text
data=' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
print(data)
