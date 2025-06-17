import pytest
from core import where_data, aggregate_data

test_data = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "poco x5 pro", "brand": "xiaomi", "price": "299", "rating": "4.4"},
]

def test_where_equal_string():
    result = where_data(test_data, "brand=apple")
    assert len(result) == 1
    assert result[0]["name"] == "iphone 15 pro"

def test_where_greater_than_number():
    result = where_data(test_data, "price>1000")
    assert len(result) == 1
    assert result[0]["name"] == "galaxy s23 ultra"

def test_where_less_than_number():
    result = where_data(test_data, "rating<4.6")
    assert len(result) == 1
    assert result[0]["name"] == "poco x5 pro"

def test_where_invalid_operator_for_string():
    with pytest.raises(ValueError):
        where_data(test_data, "brand>apple")

def test_aggregate_avg():
    result = aggregate_data(test_data, "rating=avg")
    assert result == [{"avg": 4.67}]

def test_aggregate_min():
    result = aggregate_data(test_data, "price=min")
    assert result == [{"min": 199.0}]

def test_aggregate_max():
    result = aggregate_data(test_data, "rating=max")
    assert result == [{"max": 4.9}]

def test_aggregate_invalid_column():
    with pytest.raises(ValueError):
        aggregate_data(test_data, "unknown=avg")

def test_aggregate_invalid_operator():
    with pytest.raises(ValueError):
        aggregate_data(test_data, "price=sum")

def test_aggregate_on_empty_data():
    result = aggregate_data([], "rating=avg")
    assert result == [{"avg": "Нет данных"}]