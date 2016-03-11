globalName=dict()
cp=0 # current period
def prop(func):
    ops = func() or {}
    name=ops.get('prefix','_')+func.__name__ # property name
    fget=ops.get('fget',lambda self:getattr(self, name))
    fset=ops.get('fset',lambda self,value:setattr(self,name,value))
    fdel=ops.get('fdel',lambda self:delattr(self,name))
    return property ( fget, fset, fdel, ops.get('doc','') )
def supersetattr(self,name,value):
        try:
            setattr(self,name,value)
        except AttributeError:
            super(type(self),self).__setattr__(name,value)
def supergetattr(self,name):
        try:
            getattr(self,name)
        except AttributeError:
            super(type(self),self).__getattr__(name)        

def superprop(func):
    ops = func() or {}
    name=ops.get('prefix','_')+func.__name__ # property name
    fget=ops.get('fget',lambda self:supergetattr(self, name))
    fset=ops.get('fset',lambda self,value:supersetattr(self,name,value))
    fdel=ops.get('fdel',lambda self:delattr(self,name))
    return property ( fget, fset, fdel, ops.get('doc','') )

