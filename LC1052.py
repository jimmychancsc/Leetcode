class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfied += customers[i]
        other_satisfied, best_satisfied = 0, 0
        for i, num in enumerate(customers):
            if grumpy[i] != 0:
                other_satisfied += num
            if i >= X and grumpy[i - X] != 0:
                other_satisfied -= customers[i - X]
            best_satisfied = max(best_satisfied, other_satisfied)
        return satisfied + best_satisfied