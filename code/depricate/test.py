from multipledispatch import dispatch

class Porn():
    def __init__(self):
        pass
    @dispatch (int, int)
    def pornstar(a, b):
        print(a+b)

    # @dispatch (float, float)
    # def pornstar(a, b):
    #     print(a+b)
    
    # def pornstar(self, **params):
    #     print(params['a']+params['b'])
        
        

Porn.pornstar(1, 2)
# Porn.pornstar(1.32345, 2.46434)