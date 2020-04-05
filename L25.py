mo = batRegex.search('The Adventures of Batman')

mo.group()
Out[4]: 'Batman'

mo = batRegex.search('The Adventures of Batwoman')

mo.group
Out[6]: <function Match.group>

mo.group()
Out[7]: 'Batwoman'

mo = batRegex.search('The Adventures of Batwowowowoman')
mo.group()
Out[7]: 'Batwoman'