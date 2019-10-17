# inputs
n, tmax = list(map(int, input().split()))
d = list(map(int, input().split()))
destinationXY = list(map(int, input().split()))

# main
output = 0  # Number of times that robot rided through destination point
t = 0  # Current time
i = 0  # Number of moves
# Direction of robot -> 1) Up (x stable, y increasing) 2) Right (x increasing, y stable) 3) Down (x stable, y decrasing) 4) Left (x decreasing, y stable)
XY = [0, 0]  # Current position
# Exercise require to also take in account the position at time==0
if (XY == destinationXY):
    output += 1
end = False
while True:
    stage = i % 4
    current_d = d[i % n]
    pending_t = tmax-t
    if current_d >= pending_t:
        current_d = pending_t
        end = True
    if stage == 0:
        # 1) Checks if "stable dimension" is equal to the dimension in destinationXY 2) Checks if
        if (destinationXY[0] == XY[0]) & (XY[1] < destinationXY[1]) & (XY[1]+current_d >= destinationXY[1]):
            output += 1
        XY[1] += current_d
    elif stage == 1:
        if (destinationXY[1] == XY[1]) & (XY[0] < destinationXY[0]) & (XY[0]+current_d >= destinationXY[0]):
            output += 1
        XY[0] += current_d
    elif stage == 2:
        if (destinationXY[0] == XY[0]) & (XY[1] > destinationXY[1]) & (XY[1]-current_d <= destinationXY[1]):
            output += 1
        XY[1] -= current_d
    else:  # stage == 4
        if (destinationXY[1] == XY[1]) & (XY[0] > destinationXY[0]) & (XY[0]-current_d <= destinationXY[0]):
            output += 1
        XY[0] -= current_d
    if end == False:
        t += current_d+1  # +1 because of 90 degrees rotation
        i += 1
    else:
        break
print(output)
