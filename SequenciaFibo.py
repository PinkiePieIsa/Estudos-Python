a = int(input('Digite até qual valor você deseja ver da sequência de Fibonacci: '));
p = 1;
s = 1;
n = 0;
t = [];

while n <= a:
    t = p + s;
    p = s;
    t = s;
    n +=1;
print()