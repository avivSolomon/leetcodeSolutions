
def maxPoints(points):
    max_points = 1
    for p1 in points:
        for p2 in points:
            line = [1 if ((p[1]-p1[1])*(p1[0]-p2[0]) == (p1[1]-p2[1])*(p[0]-p1[0])) else 0 for p in points] if (p1[0] - p2[0]) != 0 else [1 if p[0] == p1[0] else 0 for p in points]
            print(sum(line), line)
            max_points = max(max_points, sum(line))
    return max_points

print(maxPoints([[54,153],[1,3],[0,-72],[-3,3],[12,-22],[-60,-322],[0,-5],[-5,1],[5,5],[36,78],[3,-4],[5,0],[0,4],[-30,-197],[-5,0],[60,178],[0,0],[30,53],[24,28],[4,5],[2,-2],[-18,-147],[-24,-172],[-36,-222],[-42,-247],[2,3],[-12,-122],[-54,-297],[6,-47],[-5,3],[-48,-272],[-4,-2],[3,-2],[0,2],[48,128],[4,3],[2,4]]))
