import heapq


def min_connection_cost(cables):

    if not cables:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:

        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    print(f"Мінімальні витрати: {min_connection_cost(cables)}")
