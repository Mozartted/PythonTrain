class Handler:
    """
    An Object to handle method calls from the Parser.

    The Parser would call the start() and end() methods at beginning
    and end of each Blocking

    """
    def callback(self,prefix,name,*args):
        method=getattr(self,prefix+name,None)

        if callable(method):
            return method(*args)

    def start(self,name):
        self.callback('start_',name)

    def end(self,name):
        self.callback('end_', name)

    def sub(self,name):
        return lambda match:
            self.callback('sub_',name,match) or match.group(0)

    
