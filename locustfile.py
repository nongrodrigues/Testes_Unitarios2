from locust import HttpUser, task, between

class UsuarioEva(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def verificar_health(self):
        self.client.get("/health")

    @task(1)
    def classificar_notas(self):
        payload = {"n1": 8.0, "n2": 8.0, "n3": 8.0, "idade": 20}
        with self.client.post("/api/classificar", json=payload, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Status: {response.status_code}")
            elif response.elapsed.total_seconds() > 0.2:
                response.failure(f"SLA violado: {response.elapsed.total_seconds():.3f}s")
            else:
                response.success()