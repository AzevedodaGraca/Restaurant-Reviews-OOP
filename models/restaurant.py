from models.review import Review

class Restaurant:
    """Represents a restaurant that can receive customer reviews."""

    restaurants = []

    def __init__(self, name, category):
        """Initialize a restaurant with a name, category and empty review list."""
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._reviews = []
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        """Return a human-readable string representation of the restaurant."""
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        """Print a table of all created restaurants and their average ratings."""
        print(f"{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(25)} | Status")
        for restaurant in cls.restaurants:
            print(f"{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} | {restaurant.status}")

    @property
    def status(self):
        """Return a simple active/inactive status marker for the restaurant."""
        return '⌧' if self._active else '☐'
    
    def toggle_status(self):
        """Switch the restaurant active state on or off."""
        self._active = not self._active

    def receive_review(self, customer, rating):
        """Receive a new review if the rating is in the allowed range."""
        if 0 < rating <= 5:
            review = Review(customer, rating)
            self._reviews.append(review)

    @property
    def average_rating(self):
        """Calculate and return the average rating for the restaurant."""
        if not self._reviews:
            return '-'
        sum_of_scores = sum(review._rating for review in self._reviews)
        number_of_scores = len(self._reviews)
        average = round(sum_of_scores / number_of_scores, 1)
        return average
