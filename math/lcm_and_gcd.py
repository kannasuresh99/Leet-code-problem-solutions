"""
question link: https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
"""

"""
Approach:
Sure, here it is:

---

**Formula for GCD (Greatest Common Divisor)**

The GCD of two numbers can be found using the **Euclidean Algorithm**:

1. **Euclidean Algorithm**:
   - Given two numbers ( a ) and ( b ), where ( a > b ):
   - Replace ( a ) with ( b ) and ( b ) with ( a mod b ).
   - Repeat this process until ( b ) becomes 0.
   - The GCD is the non-zero remainder when ( b ) becomes 0.

**Example:**
Let's find the GCD of 48 and 18.

1. ( 48 mod 18 = 12 )
2. ( 18 mod 12 = 6 )
3. ( 12 mod 6 = 0 )

So, the GCD of 48 and 18 is 6.

**Formula for LCM (Least Common Multiple)**

The LCM of two numbers can be found using the relationship between GCD and LCM:

[ text{LCM}(a, b) = frac{|a cdot b|}{text{GCD}(a, b)} ]

**Example:**
Let's find the LCM of 48 and 18, knowing the GCD is 6.

1. Calculate the product of the numbers: ( 48 times 18 = 864 )
2. Divide the product by the GCD: ( frac{864}{6} = 144 )

So, the LCM of 48 and 18 is 144.

**Summary**

- **GCD**: Use the Euclidean Algorithm.
- **LCM**: Use the formula ( text{LCM}(a, b) = frac{|a cdot b|}{text{GCD}(a, b)} ).

---
"""

class Solution:
    def get_gcd(self, a, b):
        gcd = float('inf')
        
        while gcd > 0:
            gcd = a % b
            if gcd == 0:
                return b
            a = b
            b = gcd    
        
    def lcmAndGcd(self, A , B):
        # code here 
        a = A
        b = B
        if B > A:
            a = B
            b = A
        gcd = self.get_gcd(a, b)
        lcm = (a*b)//gcd
        return [lcm, gcd]
    
Solution().lcmAndGcd(48, 18)