from locust import HttpUser, TaskSet, task, constant


class ReadTask(TaskSet):
    @task(1)
    def profile(self):
        self.client.get("/", verify=False)


class Read(HttpUser):
    tasks = {ReadTask: 1}
    wait_time = constant(0)
