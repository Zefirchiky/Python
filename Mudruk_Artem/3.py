<<<<<<< HEAD
from math import sin, tan
import math

n, a = map(int, input("n, m: ").split())

R = a / (2 * sin(math.pi/n))

S_t = math.pi * R**2 / n

S_o = S_t - a**2 / (4 * tan(math.pi/n))

S_total = n * S_o

=======
from math import sin, tan
import math

n, a = map(int, input("n, m: ").split())

R = a / (2 * sin(math.pi/n))

S_t = math.pi * R**2 / n

S_o = S_t - a**2 / (4 * tan(math.pi/n))

S_total = n * S_o

>>>>>>> d4a9429d8f2eeba9daf04fa2d85d8eb63d449416
print('{:.4f}'.format(S_total))