import heapq
a = [[7,10],[2,4]]

def minimumMeetingRooms(arr):
    arr.sort()
    heap = []
    rooms = 1
    heapq.heappush(heap, arr[0][1])
    for i in range(1, len(arr)):
        prev_meet_end_time = heap[0]
        curr_meet_start_time = arr[i][0]

        if prev_meet_end_time >= curr_meet_start_time:
            rooms += 1
        else:
            heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

    return rooms

print(minimumMeetingRooms(a))