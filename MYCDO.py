from xml.dom import minidom
import sys
import getopt
from  collections import MutableMapping
from collections import MutableSequence
from cdoconfig import globalName
from cdoconfig import prop

##================================================================
## Class WaterfallStep
## Purpose  : A class for steps of a waterfall
## Version  : 1.0
## Used by  : 
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================
class MyWaterfallStep(object):
    def __init__(self):
        self._action=None
        self._condition=None
        self._payable=None
        self._receivable=None
        self._amount=None
        self._cap=None

    @prop
    def action():pass
    @prop
    def condtion():pass
    @prop
    def payable():pass
    @prop
    def receivable():pass
    @prop
    def amount():pass
    @prop
    def cap():pass
    
##================================================================
## Class Waterfall
## Purpose  : A class for  holding steps of a waterfall
## Version  : 1.0
## Used by  : 
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================
class MyWaterfall(MutableMapping):
    def __init__(self):
        self._name=None
        self._steps=dict()
      
        
        
    def __setitem__(self,key,value):
        self._steps[key]=value
    def __getitem__(self,key):
        return self._steps[key]
    def __delitem__(self,key):
        del self._steps[key]
    def __iter__(self):
        return self._steps.__iter__()
    def __len__(self):
        return len(self._steps)

  

    @prop
    def name():pass
    @prop
    def condtion():pass
    @prop
    def payable():pass
    @prop
    def receivable():pass
    @prop
    def amount():pass
    @prop
    def cap():pass


