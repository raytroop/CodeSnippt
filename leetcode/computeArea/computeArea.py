# Find the total area covered by two rectilinear rectangles in a 2D plane.

# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

# Example:

# Input: -3, 0, 3, 4, 0, -1, 9, 2
# Output: 45
# Note:
# Assume that the total area is never beyond the maximum possible value of int.

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_a = (C - A) * (D - B)
        area_b = (G - E) * (H - F)
        x_min = max(A, E)
        y_min = max(B, F)
        x_max = min(C, G)
        y_max = min(D, H)
        x = max(x_max - x_min, 0)
        y = max(y_max - y_min, 0)
        overlap = x*y
        return area_a + area_b - overlap

if __name__ == '__main__':
    solver = Solution()
    print(solver.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))

