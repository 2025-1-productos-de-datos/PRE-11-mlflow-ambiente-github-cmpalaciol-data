import os


def test_01():
    assert os.path.exists("MLproject.txt"), "El archivo MLproject.txt no existe."
