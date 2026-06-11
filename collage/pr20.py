class Power:
    def pow(self, x, n):
        # Handle negative powers
        if n < 0:
            return 1 / self.pow(x, -n)
        
        result = 1
        for _ in range(n):
            result *= x
        return result


# ---- Testing the class ----
obj = Power()
print("pow(2, 5) =", obj.pow(2, 5))   # 32
print("pow(3, 3) =", obj.pow(3, 3))   # 27
print("pow(5, 0) =", obj.pow(5, 0))   # 1
print("pow(2, -3) =", obj.pow(2, -3)) # 0.125