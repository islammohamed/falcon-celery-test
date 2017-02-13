import falcon
from resources.resource import PersistenceResource


api = falcon.API()
api.add_route('/', PersistenceResource())