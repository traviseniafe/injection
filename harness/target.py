class MockTarget:
    def __init__(self, response: str):
        self.response = response

    def respond(self, prompt: str) -> str:
        return self.response

class OpenAITarget:
    def __init__(self, model: str, instructions: str, client=None):
        if client is None:
            from openai import OpenAI
            client = OpenAI()

        self.client = client
        self.model = model
        self.instructions = instructions

    def respond(self, prompt: str) -> str:
        response = self.client.responses.create(model=self.model, instructions=self.instructions, input=prompt, store=False,)
        return response.output_text