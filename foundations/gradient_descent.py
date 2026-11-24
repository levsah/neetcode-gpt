class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        ptr = init
        for n in range(iterations):
            grad = 2 * ptr
            ptr -= learning_rate * grad
        return round(ptr, 5)
        
      
        