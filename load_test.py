from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_add(self):
        self.client.get('/add?a=2&b=3')

    @task
    def test_hello(self):
        self.client.get('/hello')
