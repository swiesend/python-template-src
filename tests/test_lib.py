from project import lib

def test_hello():

    assert True == True

    assert True is not False

    assert lib.hello() == None

    assert lib.hello("world") == None

    assert lib.hello(hello="world") == None
