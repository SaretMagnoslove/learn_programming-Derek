class DogNameError(Exception):

    def __init__(self,*args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    DogName = input('Enter a dog name pls: ')
    if any(char.isdigit() for char in DogName):
        raise DogNameError
except DogNameError:
    print('Your dog name Sucks!!! (not sorry for that btw)')