""" Main file for the module. """
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

class RateMyProfessor:
    """ Main api wrapper class. """
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.transport = AIOHTTPTransport(
            url="https://www.ratemyprofessors.com/graphql",
            headers={"authorization": f"Basic {self.auth_token}"}
        )
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)
