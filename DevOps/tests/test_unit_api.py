
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions


class testApi():
    def test_api_add(self):
        client = Client("http://localhost:5000/#/actions/calculate")
        res = calculate.sync(client=client, body=Calculation(operation= Opertions.ADD , operand1=1, operand2=1))
        assert res.result==2
    def test_api_subb(self):
        client = Client("http://localhost:5000/#/actions/calculate")
        res = calculate.sync(client=client, body=Calculation(operation= Opertions.SUBTRACT , operand1=1, operand2=1))
        assert res.result==0
    def test_api_divide(self):
        client = Client("http://localhost:5000/#/actions/calculate")
        res = calculate.sync(client=client, body=Calculation(operation= Opertions.DIVIDE , operand1=6, operand2=2))
        assert res.result==3
    def test_api_multply(self):
        client = Client("http://localhost:5000/#/actions/calculate")
        res = calculate.sync(client=client, body=Calculation(operation= Opertions.MULTIPLY , operand1=1, operand2=4))
        assert res.result==4
        
        