"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""

text = 'qwe qweабв hkjdfgu drghаабв'

word_list = text.split()

result_text = filter(lambda word: 'абв' not in word, word_list)

print(' '.join(result_text))