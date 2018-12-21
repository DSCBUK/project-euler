import numpy as np
print(np.sum([x for x in range(1001) if x % 3 == 0 or x % 5 == 0]))
