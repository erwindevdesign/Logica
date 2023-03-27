def complete_name(name, last_name, invert=False):
    if invert:
        return f'{last_name} {name}'
    else:
        return f'{name} {last_name}'
    
nameone = complete_name('Erein', 'Wills')
nametwo = complete_name('Erein', 'Wills', invert=True)
namethree = complete_name(last_name='Wills', name='Erein')

print(nameone)
print(nametwo)
print(namethree)