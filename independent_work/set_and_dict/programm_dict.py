dict = { 
    "apple" : "яблоко", 
    "bold" : "жирный", 
    "bus" : "автобус",
    "cat" : "кошка", 
    "car" : "машина"} 
print("=" * 15, "Dict", "=" * 15) 
word = "" 
while word != "q": 
    word = input("Введите слово или q для выхода: ") 
    if word != "q": 
        if word in dict: 
            print(dict[word]) 
        else: 
            print("He найдено") 