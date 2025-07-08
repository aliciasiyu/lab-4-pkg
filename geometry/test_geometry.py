import pytest
from geometry import Square, Circle, area_stats
from geometry import shapes, utils

def test_square_area_zero_and_positive():
    # Arrange: create squares with side 0 and positive values
    square_zero = Square(0)
    square_positive = Square(3)

    # Act: calculate areas
    area_zero = square_zero.area()
    area_positive = square_positive.area()

    # Assert: check areas are correct
    assert area_zero == pytest.approx(0), "Area of square with side 0 should be 0"
    assert area_positive == pytest.approx(9), "Area of square with side 3 should be 9"


def test_stats_keys_and_values():
    # Arrange: create shapes
    square = Square(2)
    circle = Circle(1)

    # Act: calculate area stats
    stats = area_stats(square, circle)

    # Assert: check keys and values
    assert set(stats.keys()) == {"n", "total", "mean", "min", "max"}, "Keys do not match expected"
    assert stats["n"] == 2, "Number of shapes should be 2"
    assert stats["total"] == 13.283185307179586, "Total area should be approximately 13.28"
    assert stats["mean"] == 6.641592653589793, "Mean area should be approximately 6.64"
    assert stats["min"] == 4, "Minimum area should be 4 (square)"
    assert stats["max"] == pytest.approx(9.869604401089358), "Maximum area should be approximately 9.87 (circle)"

def test_stats_raises_without_shapes():
    # Act & Assert: check that ValueError is raised when no shapes are provided
    with pytest.raises(ValueError, match="At least one shape must be provided."):
        area_stats()