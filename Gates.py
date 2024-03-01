def AND_gate (a, b):
    if a == 1 and b == 1:
        return 1#True
    else:
        return 0#False
print(AND_gate(1,0))

def NOT_gate(a):
    if a == 1:
        return 0
    else:
        return 1
def OR_gate (a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0