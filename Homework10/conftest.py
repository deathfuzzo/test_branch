import pytest
from datetime import datetime
import time

@pytest.fixture(autouse=True, scope="class")conftest
def print_time_start_end():
    print("\nНачало тестов:", datetime.now().strftime("%H:%M:%S"))
    yield
    print("Окончание тестов:", datetime.now().strftime("%H:%M:%S"))


@pytest.fixture(autouse=False)
def print_time_process():
    start_time = datetime.now().strftime("%H:%M:%S")
    start_time = datetime.strptime(start_time, "%H:%M:%S")
    yield
    end_time = datetime.now().strftime("%H:%M:%S")
    end_time = datetime.strptime(end_time, "%H:%M:%S")
    print("Время выполнения теста:", end_time - start_time)

