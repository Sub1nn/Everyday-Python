class Snake:
    '''Snake main blueprint'''
    # name = 'Anaconda'
    def __init__ (self, name):
        self.name = name

    def modifyName(self, new_name):
        '''Modify the name of the snake'''
        self.name = new_name
    
snake01 = Snake('anaconda')
print(snake01.name)  # Output: Anaconda

snake02 = Snake('Cobra')
print(snake02.name)  # Output: Cobra

# Modify the name of the snake
snake01.modifyName('Python')
print(snake01.name)  # Output: Python