from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = curr = 0
    truck_weights.reverse()
    bridge = deque()
    while truck_weights or bridge:
        second += 1
        if bridge_length < second:
            curr -= bridge.popleft()
            if curr == 0 and not truck_weights:
                break
        if len(bridge) < bridge_length:
            bridge.append(0)
            if truck_weights and curr+truck_weights[-1] <= weight:
                curr += truck_weights[-1]
                bridge[-1] = truck_weights.pop()
    return second
