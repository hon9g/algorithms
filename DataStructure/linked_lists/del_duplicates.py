from doubly_linked_list_from_scratch import DoublyLinkedList


def solution(ll):
    outer = ll.head
    while outer:
        inner = outer.next_node
        while inner:
            if outer.data == inner.data:
                if not inner.next_node:
                    ll.pop()
                    break
                else:
                    p, n = inner.prev_node, inner.next_node
                    p.next_node, n.prev_node = n, p
            inner = inner.next_node
        outer = outer.next_node
    return ll


if __name__ == "__main__":
    x = [
        [1, 2, 3],
        ["a", "z", "e"],
        ["apple", "banana", "monkey"],
        [1, 1, 3],
        ["a", "z", "e", "e"],
        ["apple", "banana", "banana", "monkey"],
    ]
    y = [
        [1, 2, 3],
        ["a", "z", "e"],
        ["apple", "banana", "monkey"],
        [1, 3],
        ["a", "z", "e"],
        ["apple", "banana", "monkey"],
    ]
    for t in range(len(x)):
        ll = DoublyLinkedList()
        for i in range(len(x[t])):
            ll.append(x[t][i])
        print("input:", ll)
        answer = solution(ll)
        print("output:", answer)
        print()
        for i in range(len(y[t])):
            assert y[t][i] == answer.popleft()
        assert len(answer) == 0
