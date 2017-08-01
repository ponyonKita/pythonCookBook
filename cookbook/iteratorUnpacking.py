

class A():

   def __init__(self):

        self.index = 0

   def __iter__(self):

        return self

   def __next__(self):

        self.index += 1

        if self.index > 3:

            raise StopIteration

        return 3