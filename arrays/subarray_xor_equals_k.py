"""
question link: https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258
"""

def subarraysWithSumK(a: [int], b: int) -> int:
    # Write your code here
    """
    lets assume XOR of subarray from i to j is XR
    and XOR of subaaray x to j to is b
    then,
    unknown_XR^b = XR
    (unknown_XR^b)^b = XR^b
    unknown_XR = XR^b
    """
    prefix_xor = 0
    prefix_xor_dict = {0:1}
    res = 0

    for i in range(len(a)):
        prefix_xor ^= a[i]
        unknown_xr = prefix_xor^b
        res += prefix_xor_dict.get(unknown_xr, 0)
        prefix_xor_dict[prefix_xor] = prefix_xor_dict.get(prefix_xor, 0) + 1
    
    return res

