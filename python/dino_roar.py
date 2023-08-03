"""
dino_roar.py, our main Python entry point

This script is a Python program with a main entrypoint and
main function.

It demonstrates how to use Bazel's py_binary rule to run a script
that depends on other Python files (via `py_library` items in its `deps).
"""

# Note that the full path to dino had to be specified here, as the `python` directory
# was not added as an imports directory
from python.dino import Dinosaur


def dino_roar_main():
    my_dino = Dinosaur("samasaurus", 15)

    my_dinos_roar = my_dino.get_roar()

    print("Hear my dino roar!")
    print(my_dinos_roar)


if __name__ == "__main__":
    dino_roar_main()
