import unittest
import gateio.gateio as gate


class TestClass(unittest.TestCase):
    def test_functions(self):
        test = gate.gateio({
            "apiKey": "23b8b4a24e6b093b31f94927d6f0a96e",
            "secret": "c558c602ebbb94a917bd04f2f6c830faf9a0b53d4b900af01968e7b61be668d2"
        })

        create = test.create_order("GXS_USDT", "limit", "buy", 1, price=1,
                                            params={"account": "spot", "query": {}})
        assert create['id'] is not None
        fetch = test.fetch_order(create['id'], create['symbol'], params={"account": "spot", "query": {}})
        assert fetch['id'] is not None
        cancel = test.cancel_order(create['id'], create['symbol'], params={"account": "spot", "query": {}})
        assert cancel['status'] == "cancelled"


if __name__ == '__main__':
    unittest.main()
