# Vytvořte program, který bude od uživatele načítat reálná čísla, vždy pouze jedno číslo na každém řádku. Když uživatel napíše na řádek "stop", vypíše se součet dosud zadaných čísel a program skončí. Součet vypisujte na 2 desetinná místa.

# Sample Input:
# 5
# 1.2
# 0.5
# stop

# Sample Output:
# 6.70

x = 0
y = 0
while True:
    x = str(input())
    if (x == 'stop'):
        break
    y = float(x) + float(y)

print('{:.2f}'.format(y))