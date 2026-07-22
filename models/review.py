class Review:
    """Represents a customer review with name and rating."""

    def __init__(self, customer, rating):
        """Initialize a review with the customer name and a rating."""
        self._customer = customer
        self._rating = rating
