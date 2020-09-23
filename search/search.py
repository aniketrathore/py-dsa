class Search:
    """
    This class provide interfaces to search data in
    sorted or unsorted array.
    """

    def __init__(self, items):
        if not isinstance(items, list):
            raise ValueError("Invalid data type.")
        self.items = items

    def linear_search(self, value):
        """
        Search for given data in linear time.
        Time Complexity: O(n)
        """
        if value is None:
            raise ValueError("No value provided.")
        for i, item in enumerate(self.items):
            if item == value:
                return f"{value} found at {i} location."
        return "Item not found."

    def binary_search(self, value):
        """
        Search for given data in logarithmic time.
        Array should be sorted and contain numbers.
        Time Complexity: O(log n)
        """
        items = self.items
        low, high = 0, len(items) - 1
        while low <= high:
            mid = (high + low) // 2
            if value == items[mid]:
                return f"{value} found at {mid} location."
            elif value < items[mid]:
                high = mid - 1
            elif value > items[mid]:
                low = mid + 1
        return "Item not found."

    def fast_search(self, value):
        """
        Search for given data in logarithmic time.
        Time Complexity: O(log n)
        """
        if value is None:
            raise ValueError("No value provided.")
        items = self.items
        left, right = 0, len(items) - 1
        while left <= right:
            if items[left] == value:
                return f"{value} found at {left} location."
            if items[right] == value:
                return f"{value} found at {right} location."
            left += 1
            right -= 1
        return "Item not found."
