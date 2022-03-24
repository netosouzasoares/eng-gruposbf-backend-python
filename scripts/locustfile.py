from locust import HttpUser, task
import random


def get_requests():
    return [
        {'price': 200.20},
        {'price': 999.20},
        {'price': 1.20},
        {'price': 500.20},
        {'price': 210.20},
        {'price': 20.20},
        {'price': 0.05},
        {'price': 1.20},
        {'price': 0.20},
        {'price': 30},
        {'price': 1.20},
        {'price': 2020.20},
        {'price': 10.20}
    ]


class Converter(HttpUser):
    result = get_requests()

    @task
    def send_request(self):
        self.client.post("/converter", json=random.choice(self.result))
