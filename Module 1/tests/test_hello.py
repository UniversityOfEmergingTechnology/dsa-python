from hello_updated import hello

def test_hello_with_argument():
    assert hello("Python") == "Hello , Python"

def test_hello_default():
    assert hello() == "Hello , world"