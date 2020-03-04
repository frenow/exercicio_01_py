matheusalcantarasousa@gmail.com
set: coleção não ordenada sem duplicidade
a = {1, 2, 3, 4}
assim como a tupla e a lista eles contém dados (os três são "containers") - mas os dados não tem uma ordem: não importa em que ordem você coloca os dados em um conjunto, você só pode pegar de volta ou um dado aleatório, ou percorrer todos os elementos (com um for), mas numa ordem desconhecida.


tuple: alguns valores separados por virgula
a = (1, 2, 3, 4)
A tupla é uma sequência imutável: isso é, depois de criada, ela não pode mais ser alterada.



como usar listas... (https://docs.python.org/3.4/tutorial/datastructures.html#using-lists-as-stacks)
...como usar fila (ou queue)
FIFO (first-in first-out), ou seja, “primeiro a entrar, primeiro a sair”.
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

...como usar pilha (ou stack)
A Stack usa o sistema LIFO (last-in first-out), ou seja, “último a entrar, primeiro a sair”.
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]


O que o statement else faz em um loop?
R: quando ocorrer o break da iteração for x in range(2,n) o else não executa a instrução print(n, 'is a prime number'). 
Serve para um controle da sequencia do break em for ou while

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print (n,'equals',x,'*',n//x)
            break
    else:
        print(n, 'is a prime number')