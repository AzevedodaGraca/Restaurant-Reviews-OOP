# Restaurant Review Project

This project implements a simple restaurant review system in Python.
This is my first object-oriented Python project and demonstrates classes, methods, and properties.

## Features

- `Restaurant` class stores restaurant name, category, active status, and customer reviews.
- `Review` class stores a customer name and a numeric rating.
- The code prints a table of restaurants with average ratings and active/inactive status.
- Ratings are only stored when they fall in the allowed range: `0 < rating <= 5`.

## Files

- `app.py`: Creates a sample restaurant, adds reviews, and prints the restaurant list.
- `models/restaurant.py`: Defines the `Restaurant` class and the main business logic.
- `models/review.py`: Defines the `Review` class.
- `models/__init__.py`: Package initializer for the `models` package.

## How it works

1. `app.py` imports `Restaurant` from `models.restaurant`.
2. A `Restaurant` object is created with name and category.
3. Reviews are added using `receive_review(customer, rating)`.
4. `Restaurant.list_restaurants()` prints a formatted table of restaurants.

## Running the project

From the project root:

```bash
python3 app.py
```

## Notes

- The restaurant example in `app.py` uses ratings `10`, `8`, and `2`.
- Because the current logic only accepts ratings between `1` and `5`, only the review with rating `2` is stored.
- The average rating is calculated from stored reviews and displayed with one decimal place.
