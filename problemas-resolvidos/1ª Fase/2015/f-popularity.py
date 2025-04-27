################################################################################
# Objetivo: Dadas uma lista de strings e uma lista de nomes linguagens de 
#           programação, calcular quantas vezes cada linguagem aparece nas strings
# 
# Autor: Rodrigo
# Data: 14/03/2025
# Duração: 9min
################################################################################
posts = list()
languages = dict()

qtd_posts = int(input())
for _ in range(qtd_posts):
    posts.append(input())
    
qtd_languages = int(input())    
for _ in range(qtd_languages):
    lang = input()
    languages[lang] = 0

for post in posts:
    for lang in languages.keys():
        lang_str = " " + lang + " "
        if lang_str.lower() in post.lower():
            languages[lang] += 1     
            
# output
for lang in languages.keys():
    print(f"{lang} {languages[lang]}")
