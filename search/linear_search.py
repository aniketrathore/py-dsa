class LinearSearch:

    """
    Linear search work with both sorted and unsorted data.
    This class provide to interface for searching.
    """

    def __init__(self, items):
        if not isinstance(items, list):
            raise ValueError("Invalid data type.")
        self.items = items

    def search(self, value):
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

    def fast_search(self, value):
        """
        Search for given data in linear logarithmic time.
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


