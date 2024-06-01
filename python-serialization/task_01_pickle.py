#!/usr/bin/python3
import pickle

class CustomObject:
    """
    A class to represent a custom object.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Indicates if the object is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and student status.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Indicates if the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the details of the CustomObject.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
        Serialize the CustomObject and save it to a file.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        with open(filename, 'wb') as newfile:
            pickle.dump(self, newfile)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize the CustomObject from a file.

        Args:
            filename (str): The name of the file containing the serialized object.

        Returns:
            CustomObject: The deserialized CustomObject.
        """
        with open(filename, 'rb') as newfile:
            return pickle.load(newfile)
