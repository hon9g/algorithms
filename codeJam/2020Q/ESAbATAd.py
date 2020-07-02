import sys

def applyComplement(arr):
    return [x if x == -1 else 1-x for x in arr]

def applyReverse(arr):
    return [arr[-i] for i in range(1, len(arr)+1)]

def applyComplementAndReverse(arr):
    return applyComplement(applyReverse((arr)))


def requestQuery(index):
    print(index)
    sys.stdout.flush()
    response = input()
    return response

def checkType(arr):
    is_mirror = True
    is_complement = True
    for i in range(0, int(len(arr)/2)):
        if arr[i] == -1:
            break
        if arr[i] == arr[-i-1]:
            is_complement = False
        else:
            is_mirror = False

    return is_mirror, is_complement, not is_mirror and not is_complement # mirror, complement, combo


def determineTransformationForMirrorAndComplement(arr, i):
    valueAtI = int(requestQuery(i + 1))
    valueAtI = int(requestQuery(i + 1))
    if valueAtI != arr[i]:
        return applyComplement(arr)
    else:
        return arr

def determineTransformationForCombo(arr, sameIndex, diffIndex):
    sameIValue = int(requestQuery(sameIndex+1))
    diffIValue = int(requestQuery(diffIndex+1))

    # print("Array is ", arr)
    # print("Same and diff indices are {} {}".format(sameIndex, diffIndex))
    # print("Received values are {} {}".format(sameIValue, diffIValue))

    # 4 cases
    if sameIValue == arr[sameIndex]:
        if diffIValue == arr[diffIndex]:
            # print("No transform")
            return arr
        else:
            # print("Reverse transform")
            return applyReverse(arr)
    else:
        # print("Updated diff value is ", diffIValue)
        # print("Previous diff value is", arr[diffIndex])
        if diffIValue == arr[diffIndex]:
            # print("Complement and reverse transform")
            return applyComplementAndReverse(arr)
        else:
            # print("Complement transform")

            return applyComplement(arr)

def findSameAndDiffIndexOfArr(arr):
    if arr[0] == arr[-1]:
        same = 0
        i = 1
        while(arr[i] == arr[-i-1]): i += 1
        return same, i
    else:
        diff = 0
        i = 1
        while(arr[i] != arr[-i-1]): i += 1
        return i, diff


def solveForArr(B):
    arr = [-1 for i in range(B)]
    queryCount = 0
    queryIndex = 1
    while(arr.count(-1) != 0):
        # We haven't discovered the full array yet
        # print("Query count is ", queryCount)
        if queryCount % 10 == 0 and queryCount > 0:
            # Gotta check what transformation was made to the data
            typeOfCurrentData = checkType(arr)
            if typeOfCurrentData[0] or typeOfCurrentData[1]:
                # is mirror or is complement
                arr = determineTransformationForMirrorAndComplement(arr, 0)
                queryCount += 2
            else:
                # Find same and diff index
                same, diff = findSameAndDiffIndexOfArr(arr)
                arr = determineTransformationForCombo(arr, same, diff)
                queryCount += 2

        # Regardless of if we need to check our result or not, we query for new data
        # Find start and end
        arr[queryIndex-1] = int(requestQuery(queryIndex))
        arr[B-queryIndex] = int(requestQuery(B-queryIndex+1))
        queryCount += 2
        queryIndex += 1
        # print("Query count is now ",queryCount)

    return arr


T, B = input().split(" ")
T = int(T)
B = int(B)
for _ in range(T):
    answer = solveForArr(B)
    response = requestQuery("".join([str(x) for x in answer]))
    if response == "N":
        exit()