class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        ptr = init 
        for _ in range(iterations):
            deriv = 2 * ptr 
            ptr = ptr - learning_rate * deriv

        return round(ptr, 5)
        
      
        