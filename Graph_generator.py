import Game_for_Test as GT
import matplotlib.pyplot as plt
import numpy as np

M = int(input('Please input times:'))
times = np.arange(0, M+1, 10000)
score = []
for i in range(1, len(times)):
    win, loss, tie = GT.Simulator(times[i], 17)
    score.append((2 * win + tie - loss) / times[i])
    print(score)

x = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
list15 = [0.422, 0.437, 0.438, 0.418, 0.437, 0.432, 0.430, 0.432, 0.430, 0.432]
list16 = [0.440, 0.434, 0.440, 0.445, 0.435, 0.439, 0.440, 0.4395, 0.439, 0.440]
list17 = [0.440, 0.422, 0.442, 0.426, 0.420, 0.430, 0.4294, 0.4288, 0.4292, 0.4295]

plt.plot(x, list15, label="stand point=15", color="green", marker=".", linestyle="--")
plt.plot(x, list16, label="stand point=16", color="red", marker="+", linestyle="-")
plt.plot(x, list17, label="stand point=17", color="blue", marker="x", linestyle=":")
plt.xlabel('Times')
plt.ylabel('Score')
plt.legend()
plt.show()
# M = int(input("TIMES:"))
# N = int(input('STEPS:'))
# times = np.arange(1, M + 1, N)
# for t in times:
#     win, loss, tie = GT.Simulator(t, 17)
#     print(f'Threshold:{17}')
#     print(f'TIMES:{t}')
#     print(f'Final score:{(2 * win + tie - loss)/t}')
#     print('\n')
