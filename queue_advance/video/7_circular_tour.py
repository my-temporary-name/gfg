# First circular tour that visits all petrol pumps
# ex: Petrol = [4, 8, 7, 4] and distance = [6, 5, 3, 5]. O/p: 2
# we have circular arrangement of petrol pumps. We need to find the first petrol pump from where we can visit all petrol pumps.


from collections import deque

def printTour(pet, dist):
    n = len(pet)
    for start in range(n):
        curr_pet = 0
        end = start

        while True:
            curr_pet += (pet[end] - dist[end])
            if curr_pet<0:
                break
            end = (end+1)%n
            if end == start:
                return start+1
    return -1

pet = [4, 8, 7, 4]
dist = [6, 5, 3, 5]
print(printTour(pet,dist))


# Efficient solution:
# We can use the concept of deque here.
# Idea is to maintain a deque of size n and store the difference of petrol and distance in the deque.

def printTour2(pet,dist):
    n = len(pet)
    start =0
    curr_pet = 0
    prev_pet = 0

    for i in range(n):
        curr_pet += (pet[i] - dist[i])
        if curr_pet<0:
            start = i+1
            prev_pet += curr_pet
            curr_pet = 0
    return start+1 if ((curr_pet + prev_pet)>=0) else 1

pet = [4, 8, 7, 4]
dist = [6, 5, 3, 5]
print(printTour2(pet,dist))
