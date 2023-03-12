from pytorch_gpu_mnist import add

# fake test to try github actions without eating up credits training on mnist
def test_add():
    assert add(2, 3) == 5
