import numpy as np
from matplotlib import pyplot as plt
from constants import videoformatting

s = "This is a test string containing random variables 1234567890 !@#$%^&*_+-=;:<>,. a"

l = len(s)

# print(videoformatting.variables("prod", quality="1080", frames="30", colour=True))

arr = []

for i in range(l):
    arr.append(ord(s[i]))

n = np.array(arr)

n = n.reshape((9,9))

plt.imshow(n, interpolation='nearest')
plt.savefig('./Video/test.png')
# plt.show()