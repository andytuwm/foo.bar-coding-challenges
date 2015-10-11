def answer(intervals):
    min,max = intervals[0]
    for shift in intervals:
        if shift[0] < min:
            min = shift[0]
        if shift[1] > max:
            max = shift[1]
    return max - min