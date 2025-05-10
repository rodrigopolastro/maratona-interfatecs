import copy

nestedObject = {
    "a": {'primeiro': 1},
    "b": {'segundo': 2},
    "c": {'terceiro': 3}
}

# => esse objeto é apenas um ponteiro para o objeto original
shallowCopy = copy.copy(nestedObject) 
shallowCopy['a']['primeiro'] = 'duplicado'
# => {'a': {'primeiro': 'duplicado'}, 'b': {'segundo': 2}, 'c': {'terceiro': 3}}
# => {'a': {'primeiro': 'duplicado'}, 'b': {'segundo': 2}, 'c': {'terceiro': 3}}

# => somente usando uma cópia profunda um objeto realmente novo criado
deepCopy = copy.deepcopy(nestedObject) 
deepCopy['a']['primeiro'] = 'sem duplicação'
# => {'a': {'primeiro': 'duplicado'}, 'b': {'segundo': 2}, 'c': {'terceiro': 3}}
# => {'a': {'primeiro': 'sem duplicação'}, 'b': {'segundo': 2}, 'c': {'terceiro': 3}}

print(1, nestedObject)
print(2, shallowCopy)
print()
print(1, nestedObject)
print(3, deepCopy)