"""
Example Python "dino" library.

This file is mainly meant to showcase how to use a Python "library" within
another Python script in Bazel.

What is a Python library? A Python library is a Python module that is never
intended to be the main entrypoint of a Python program. Instead, its
use is limited to being imported into other programs.

This library creates the Dino class, which has a few basic functions.
This library is standalone, meaning it does not require other libraries in
this project. This will be reflected in the `deps` field of its `py_library`
declaration.

Why dino? Because dinosaurs are great even for adults :sunglasses:.
"""

class Dinosaur:

    def __init__(self, species: str, num_legs: int) -> None:
        """
        Create a Dinosaur instance.

        Args:
            species: The species of dinosaur, such as "T-Rex" or "Brachiosaurus".
            num_legs: The number of legs this dinosaur posesses. Can be negative why not.
        """
        self.species = species
        self.num_legs = num_legs

    def get_roar(self) -> str:
        """
        All dinosaurs can roar, right? This function gets the roar of the particular dinosaur.
        """
        roar = f"I am a {self.species}, cower in fear before the stomp of my {self.num_legs} legs!"

        return roar
