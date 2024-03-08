import sys

n, m = map(int, input().split())

fire = list(map(int, input().split()))
station = list(map(int, input().split()))

ans = -1

for fire_location in fire:
    Min = sys.maxsize
    for station_location in station:
        dist = abs(fire_location - station_location)
        Min = min(Min, dist)
    ans = max(ans, Min)

print(ans)