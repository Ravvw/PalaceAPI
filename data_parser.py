from curl_cffi import requests

base_url = 'https://palacenft.com/api/v1/'
packs_path = 'markets/packs?collection_id={}'
check_path = 'users/check'
commission_path = 'markets/commission'
buy_path = 'markets/{}/buy'
offers_path = 'markets/offers?collection_id={}&limit={}&offset={}&sort={}'
collections_path = 'markets/collections?onSale={}'


class DataParser:

    def __init__(self, init_user_data):
        self.headers = {
            "Content-Type": "application/json",
            "x-user-data": init_user_data
        }

    def update_user_data(self, new_user_data):
        self.headers['x-user-data'] = new_user_data

    def check_role(self):
        result = requests.post(base_url + check_path, impersonate="chrome",  headers=self.headers)
        return result.json()

    def get_commission(self):
        result = requests.get(base_url + commission_path, impersonate="chrome",  headers=self.headers)
        return result.json()

    def get_packs(self, collection: int):
        result = requests.get(base_url + packs_path.format(collection), impersonate="chrome",  headers=self.headers)
        return result.json()

    def get_offers(self, collection: int, limit: int = 40, offset: int = 0, sort: str = 'price_asc') -> {}:
        result = requests.get(base_url + offers_path.format(collection, limit, offset, sort),
                              impersonate="chrome",  headers=self.headers)
        return result.json()

    def buy(self, offer: int):
        result = requests.post(base_url + buy_path.format(offer), impersonate="chrome",  headers=self.headers)
        return result.json()

    def get_collections(self, on_sale: bool = True):
        result = requests.get(base_url + collections_path.format(on_sale), impersonate="chrome",  headers=self.headers)
        return result.json()

    # def wallets(self):
    #     result = requests.post(base_url + 'wallets', impersonate="chrome",  headers=self.headers)
    #     return result.json()
