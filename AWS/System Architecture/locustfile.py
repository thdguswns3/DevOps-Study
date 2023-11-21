from locust import task, FastHttpUser, between

class User(FastHttpUser):
    wait_time = between(1, 1.5)

    @task
    def index(self):
        self.client.get("/")
