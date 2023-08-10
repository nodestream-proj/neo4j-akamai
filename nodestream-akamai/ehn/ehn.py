import logging

from akamai_utils.client import AkamaiApiClient

from nodestream.pipeline.extractors import Extractor


class AkamaiEHNExtractor(Extractor):
    def __init__(self, **akamai_client_kwargs) -> None:
        self.client = AkamaiApiClient(**akamai_client_kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def extract_records(self):
            try:
                for edge_hostname in self.client.list_edge_hostnames():
                    edge_hostname['edgeHostname'] = edge_hostname['recordName'] + '.' + edge_hostname['dnsZone']
                    yield edge_hostname
            except Exception as err:
                self.logger.error("Failed to list edge hostnames: %s", err)