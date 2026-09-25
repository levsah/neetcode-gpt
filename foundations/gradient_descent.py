class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        startPt = init
        for _ in range(iterations):
            deriv = 2 * startPt
            startPt = startPt - learning_rate * deriv
      
        return round(startPt, 5)