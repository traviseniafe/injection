class MockTarget:
    def __init__(self, response: str):
        self.response = response

    def respond(self, prompt: str) -> str:
        return self.response