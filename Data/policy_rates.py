from data.fetchers.base_fetcher import BaseFetcher

class PolicyRatesFetcher(BaseFetcher):
    def fetch(self):
        raw = {
            "effr": 5.33,
            "cpi_yoy": 3.1
        }
        return raw

    def normalize(self, raw):
        return {
            "effr": float(raw["effr"]),
            "cpi_yoy": float(raw["cpi_yoy"])
        }
