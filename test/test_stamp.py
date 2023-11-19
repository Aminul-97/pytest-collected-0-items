import pytest
from src.stamp import timestamp_using_time, timestamp_using_datetime, convert_timestamp, custom_timestamp

@pytest.fixture()
def get_timestamp_using_time():
    return timestamp_using_time()

@pytest.fixture()
def get_timestamp_using_datetime():
    return timestamp_using_datetime()

def test_validity(get_timestamp_using_time, get_timestamp_using_datetime):
    assert convert_timestamp(get_timestamp_using_time) == convert_timestamp(get_timestamp_using_datetime)

def test_custom_timestamp():
    assert 