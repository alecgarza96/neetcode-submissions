class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for num in nums:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1
        return sorted(elements, key=elements.get, reverse=True)[:k]

        