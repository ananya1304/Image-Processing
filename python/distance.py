import numpy as np
import math

mat=np.array([[1,1,0,0,1,1],[1,1,0,0,0,1]])
print("Enter coordinates of P")
xp=int(input())
yp=int(input())
print("Enter coordinates of Q")
xq=int(input())
yq=int(input())
euclidian_dist=math.sqrt((xp-xq)**2+(yp-yq)**2)
manhattan_dist=abs(xp-xq)+abs(yp-yq)
chessboard_dist=max(abs(xp-xq),(yp-yq))
print("Euclidian distance = "+str(euclidian_dist))
print("Manhattan distance = "+str(manhattan_dist))
print("Chess board distance = "+str(chessboard_dist))