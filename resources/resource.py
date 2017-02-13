from resources.tasks import hello
class PersistenceResource():
    def __init__(self):
        pass

    def on_get(self, request, response):
        hello.delay()
        response.body = "data saved"
