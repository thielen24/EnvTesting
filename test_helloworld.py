import helloworld as hw


def test_helloworld():
    assert hw.helloworld() == "Hello World!"

def test_add():
    assert hw.add(2, 3) == 5
