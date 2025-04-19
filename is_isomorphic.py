'''
Реализовать функцию (или тело функции), которая проверяет на изоморфность два слова. 

Пояснение: строки s и t называются изоморфными, если все вхождения каждого символа строки s 
можно последовательно заменить другим символом и получить строку t. 
Порядок символов при этом должен сохраняться, а замена — быть уникальной. Так, два разных 
символа строки s нельзя заменить одним и тем же символом из строки t, 
а вот одинаковые символы в строке s должны заменяться одним и тем же символом.
'''

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for s_char, t_char in zip(s, t):
        if s_char in s_to_t:
            if s_to_t[s_char] != t_char:
                return False
        else:
            s_to_t[s_char] = t_char
        
        if t_char in t_to_s:
            if t_to_s[t_char] != s_char:
                return False
        else:
            t_to_s[t_char] = s_char
    
    return True


s = 'paper'
t = 'title'
print(is_isomorphic(s, t))  # True

# Оптимальность решения по времени O(n) и памяти O(1)
