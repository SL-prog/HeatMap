from matplotlib.animation import FuncAnimation
from pylab import * #couleurs

n = 58

map = np.ones((n,n))

temp_init = 150 #temperature au centre
map[math.floor(n/2), math.floor(n/2)] = temp_init

#map[math.floor(n/2)-1, math.floor(n/2)] = 0
#map[math.floor(n/2)+1, math.floor(n/2)] = 7
#map[math.floor(n/2), math.floor(n/2)-1] = 10
#map[math.floor(n/2), math.floor(n/2)+1] = 7

for x in range(0, n): #definition des bords
    map[0, x] = 20.5
    map[x, 0] = 20.5
    map[x, n-1] = 20.5
    map[n-1, x] = 20.5

c = 1
def run(i):
    map2 = np.copy(map)
    for x in range(1, n-1):
        for y in range (1, n-1):
            box = map[x, y] #case T_ij a l'instant t
            dt = c*((map[x, y+1] - box) + (map[x, y-1] - box)
                    + (map[x+1, y] - box) + (map[x-1, y] - box))
            map2[x, y] = abs(dt) - map[x, y] #matrice a l'instant t+1


    for x in range(1, n-1):
        for y in range (1, n-1):
            map[x, y] = map2[x, y]
    matrix.set_array(map2)


fig, ax = plt.subplots()
matrix = ax.matshow(map, cmap = cm.jet)
ani = FuncAnimation(fig, run, interval=100)

plt.show()