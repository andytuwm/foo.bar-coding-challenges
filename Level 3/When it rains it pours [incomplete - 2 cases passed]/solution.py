trapped_water = 0


def findHighest(arr, start):
    max = -1
    max_index = len(arr) - 1
    start += 1
    for i, el in enumerate(arr[start:]):
        i += start
        if el > max:
            max = el
            max_index = i
    return max_index, max


# find the next higher or equal wall and return the index and height, if not found, return -1
def findNextHigherMax(arr, start, left_height):
    start += 1
    for i, el in enumerate(arr[start:]):
        i += start
        if el >= left_height:
            return i, el
    return -1, -1


def rightSideBoundary(arr, start, left_bound):
    global trapped_water
    if start == len(arr) - 1:
        return trapped_water
    if arr[start + 1] == left_bound:
        return rightSideBoundary(arr, start + 1, left_bound)
    next_wall_index, next_wall_height = findHighest(arr, start)
    smaller_max = min(left_bound, next_wall_height)
    for height in arr[start:next_wall_index]:
        water = smaller_max - height
        if water > 0:
            trapped_water += water
    return rightSideBoundary(arr, next_wall_index, next_wall_height)


def getTrappedWater(arr, start, left_bound):
    next_index, right_wall = findNextHigherMax(arr, start, left_bound)
    global trapped_water
    if next_index > -1:
        smaller_max = min(left_bound, right_wall)
        for i, el in enumerate(arr[start:next_index]):
            water = smaller_max - el
            if water > 0:
                trapped_water += water
        return getTrappedWater(arr, next_index, right_wall)
    elif start == len(arr) - 1:
        return trapped_water
    else:
        return rightSideBoundary(arr, start, left_bound)


def answer(heights):
    if len(heights) > 2:
        return getTrappedWater(heights, 0, heights[0])
    return 0


# hut = [3, 1, 2, 5, 1, 2, 4, 3]
# hut = [1, 4, 2, 5, 1, 2, 3]
# hut = [3, 1, 1, 1, 5]
# hut = [3, 1, 2, 2, 1, 3]
# hut = [4, 1, 2, 5, 5, 2, 5]
# hut = [1, 2, 3, 2, 1]
# hut = [5, 3, 2, 4, 7, 5, 4, 3]
# hut = [1, 2, 2, 2, 2, 1]
# hut = [3, 1, 1, 4, 1, 2, 1, 3, 2, 1, 1, 5]
hut = [1, 2, 3, 1, 2, 1, 1, 5, 3, 1, 2, 1]

print(answer(hut))
