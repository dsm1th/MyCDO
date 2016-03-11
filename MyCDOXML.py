from xml.dom import minidom
import sys
import getopt
from  collections import MutableMapping
from collections import MutableSequence
from cdoconfig import globalName
from cdoconfig import prop



class MyXMLWaterfalls(MutableMapping):
    def __init__(self):
        self._wfs=dict()
      
        
        
    def __setitem__(self,key,value):
        self._wfs[key]=value
    def __getitem__(self,key):
        return self._wfs[key]
    def __delitem__(self,key):
        del self._wfs[key]
    def __iter__(self):
        return self._wfs.__iter__()
    def __len__(self):
        return len(self._wfs)

    @prop
    def name():pass

class MyXMLWaterfall(MutableMapping):
    def __init__(self):
        self._steps=dict()
        self._name=""
        
        
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


class MyXMLWaterfallStep(object):
    def __init__(self):
       self._condition=""
       self._action=""
       self._logic=""
       self._payable=""
       self._receivable=""
       self._amount=""
       self._cap=""

    @prop
    def action():pass
    @prop
    def condition():pass
    @prop
    def action(): pass
    @prop
    def logic():pass
    @prop
    def payable():pass
    @prop
    def receivable():pass
    @prop
    def amount():pass
    @prop
    def cap():pass
    
    
class MyXMLHedge(MutableMapping):
    
    def __init__(self):
        self._legs=dict()
        self._name=""
        self._stype=""
        self._state=""
        self._upfrontfee=0.0
        
    def __setitem__(self,key,value):
        self._legs[key]=value
    def __getitem__(self,key):
        return self._legs[key]
    def __delitem__(self,key):
        del self._legs[key]
    def __iter__(self):
        return self._legs.__iter__()
    def __len__(self):
        return len(self._legs)

    @prop
    def name():pass
    @prop
    def stype():pass

    @prop
    def state():pass

    @prop
    def upfrontfee():pass

class MyXMLLeg(object):

    def __init__(self):
        self._ltype=""
        self._assetname=""
        self._notional=()
        self._coupon=()
    @prop
    def assetname():pass
    @prop
    def notional():pass
    @prop
    def ltype():pass
    @prop
    def coupon():pass

class MyXMLTranches(MutableMapping):
    def __init__(self):
        self._tranches=dict()
    def __setitem__(self,key,value):
        self._tranches[key]=value
    def __getitem__(self,key):
        return self._tranches[key]
    def __delitem__(self,key):
        del self._tranches[key]
    def __iter__(self):
        return self._tranches.__iter__()
    def __len__(self):
        return len(self._tranches)

class MyXMLTranche(object):
    def __init__(self):
        self._name=""
        self._ttype=""
        self._currency=()
        self._notional=()
        self._coupon=()
        self._ocratio=()
        self._ratioformula=()
        self._icratio=()
        self._icratioformula=()
        self._icpaydown=()
        self._pricingfactor=1
        self._pricingmethod=""
        self._discountmargin=0.0
    @prop
    def name() :pass 
    @prop
    def ttype():pass
    @prop
    def currency(): pass
    @prop
    def notional(): pass
    @prop
    def coupon(): pass
    @prop
    def ocratio(): pass
    @prop
    def ratioformula(): pass
    @prop
    def icratio(): pass
    @prop
    def icratioformula(): pass
    @prop
    def icpaydown(): pass
    @prop
    def pricingfactor():pass
    @prop
    def pricingmethod(): pass
    @prop
    def discountmargin():pass
        
class MyXMLHedges(MutableMapping):
    
    def __init__(self):
        self._hedges=dict()
    
        
    def __setitem__(self,key,value):
        self._hedges[key]=value
    def __getitem__(self,key):
        return self._hedges[key]
    def __delitem__(self,key):
        del self._hedges[key]
    def __iter__(self):
        return self._hedges.__iter__()
    def __len__(self):
        return len(self._hedges)

class MyXMLCashFlowParams(MutableMapping):


    def __init__(self):
        self._items=dict()
        self._name=""
        self._mode=()
        self._liborcurve=()
        self._defaultcurve=()
        self._default=()
        self._outputtype=()
        self._outputtarget=()
        self._waterfallsteps=()#single list or range or list of ranges
        
    def __setitem__(self,key,value):
        self._items[key]=value
    def __getitem__(self,key):
        return self._items[key]
    def __delitem__(self,key):
        del self._items[key]
    def __iter__(self):
        return self._items.__iter__()
    def __len__(self):
        return len(self._items)
    @prop
    def name():pass
    @prop
    def mode():pass
    @prop
    def liborcurve():pass
    @prop
    def defaultcurve():pass
    @prop
    def outputtype():pass
    @prop
    def outputtarget():pass
    @prop
    def waterfallsteps():pass

class MyXMLCFItem(object):

        def __init__(self):
            self._name=""
            self._expression=""
            self._format=MyXMLFormat()

        @prop
        def name(): pass
        @prop
        def expression():pass

        def setformat(self,form):
            self._format=form
    
class MyXMLFormat(object):
        def __init__(self):
            self._style=()
            self._numberformat=()
            self._numberformatlocal=()
            self._borders=()
            self._font=()
            self._interior=()
        @prop
        def style() : pass      
        @prop
        def numberformat():pass
        @prop
        def numberformatlocal():pass
        @prop
        def borders() : pass
        @prop
        def font():pass
        @prop
        def interior() : pass
        
class MyXMLBorder(object):
        def __init__(self):
            self._diagonaldown=()
            self._diagonalup=()
            self._edgebottom=()
            self._edgetop=()
            self._edgeleft()
            self._edgeright()
        @prop
        def diagonaldown():pass
        @prop
        def diagonalup():pass
        @prop
        def edgebottom():pass
        @prop
        def edgetop():pass
        @prop
        def edgeleft():pass
        @prop
        def edgeright():pass
        
        
class MyXMLParam(MutableMapping):
    def __init__(self):
        self._dict=dict()
    def __setitem__(self,key,value):
        self._dict[key]=value
    def __getitem__(self,key):
        return self._dict[key]
    def __delitem__(self,key):
        del self._dict[key]
    def __iter__(self):
        return self._dict.__iter__()
    def __len__(self):
        return len(self._dict)

class MyXMLRatingTableRow(MutableMapping):
    def __init__(self):
        self._dict=dict()
        self._rating=""
    def __setitem__(self,key,value):
        self._dict[key]=value
    def __getitem__(self,key):
        return self._dict[key]
    def __delitem__(self,key):
        del self._dict[key]
    def __iter__(self):
        return self._dict.__iter__()
    def __len__(self):
        return len(self._dict)
    @prop
    def rating():pass
class MyXMLMoodys(object):
    def __init__(self):
        self._parameters=MyXMLParam()
        self._vectors=dict() # diction of vectors
        self._curve=dict() # dictionary of curves
        self._prepays=dict() # dictionary of prepays
        self._scenarios=dict()#
        self._shocks=dict()
        self._ratingstable=dict()# dictionary of ratingtable rows
        self._cfparams=MyXMLParam()
        self._outputparam=MyXMLParam()
        self._cbm=MyXMLCBM()
    def addparameter(self,k,m):
        self._parameters[k]=m
    def addvector(self,k,m):
        self._vectors[k]=m
    def addcurve(self,k,m):
        self._curve[k]=m
    def addprepay(self,k,m):
        self._prepays[k]=m
    def addscenario(self,k,m):
        self._scenarios[k]=m
    def addshock(self,k,m):
        self._shocks[k]=m
    def addratingrow(self,k,m):
        self._ratingstable[k]=m
        
    def addcfparameter(self,k,m):
        self._cfparams[k]=m
    def addoutputparameter(self,k,m):
        self._outputparam[k]=m
    def setCBM(self,cbm):
        self._cbm=cbm
        
class SandP_RR(object):
    def __init__(self):
        self._name=""
        self._delay=0
        self._RR=0
    @prop
    def name():pass
    @prop
    def delay():pass
    @prop
    def rr():pass


class MyXMLSandP(object):
    def __init__(self):
        self._parameters=MyXMLParam()
        self._vectors=dict() # diction of vectors
        self._curve=dict() # dictionary of curves
        self._desiredratings=dict() 
        self._prepays=dict() # dictionary of prepays
        self._defaultscenario=dict()#
        self._RR=dict() # dictionary of SandP_RR objects
        self._hurdlerates=dict()# 
        self._cfparams=MyXMLParam()
        self._outputparam=MyXMLParam()
    def addparameter(self,k,m):
        self._parameters[k]=m
    def addvector(self,k,m):
        self._vectors[k]=m
    def addcurve(self,k,m):
        self._curve[k]=m
    def addprepay(self,k,m):
        self._prepays[k]=m
    def adddesiredrating(self,k,m):
        self._desiredratings[k]=m
    def addscenario(self,k,m):
        self._defaultscenario[k]=m
    def addRR(self,k,m):
        self._RR[k]=m
    def addhurdlerate(self,k,m):
        self._hurdlerates[k]=m
        
    def addcfparameter(self,k,m):
        self._cfparams[k]=m
    def addoutputparameter(self,k,m):
        self._outputparam[k]=m
        
class Fitch_RR(object):
    def __init__(self):
        self._name=""
        self._delay=0
        self._RR=0
    @prop
    def name():pass
    @prop
    def delay():pass
    @prop
    def rr():pass


class MyXMLFitch(object):
    def __init__(self):
        self._parameters=MyXMLParam()
        self._vectors=dict() # diction of vectors
        self._curve=dict() # dictionary of curves
        self._desiredratings=dict() 
        self._prepays=dict() # dictionary of prepays
        self._defaultscenario=dict()#
        self._RR=dict() # dictionary of SandP_RR objects
        self._hurdlerates=dict()# 
        self._cfparams=MyXMLParam()
        self._outputparam=MyXMLParam()
    def addparameter(self,k,m):
        self._parameters[k]=m
    def addvector(self,k,m):
        self._vectors[k]=m
    def addcurve(self,k,m):
        self._curve[k]=m
    def addprepay(self,k,m):
        self._prepays[k]=m
    def adddesiredrating(self,k,m):
        self._desiredratings[k]=m
    def addscenario(self,k,m):
        self._defaultscenario[k]=m
    def addRR(self,k,m):
        self._RR[k]=m
    def addhurdlerate(self,k,m):
        self._hurdlerates[k]=m
        
    def addcfparameter(self,k,m):
        self._cfparams[k]=m
    def addoutputparameter(self,k,m):
        self._outputparam[k]=m
                
class MyXMLCBM(object):
    def __init__(self):
        self._params=MyXMLParam()
        self._dict=dict()
    def addparameter(self,k,m):
        self._params[k]=m
    def __setitem__(self,key,value):
        self._dict[key]=value
    def __getitem__(self,key):
        return self._dict[key]
    def __delitem__(self,key):
        del self._dict[key]
    def __iter__(self):
        return self._dict.__iter__()
    def __len__(self):
        return len(self._dict)
    
class MyXMLAssets(MutableMapping):
    def __init__(self):
        self._assets=dict()
        self._parameters=MyXMLParam()
    def __setitem__(self,key,value):
        self._assets[key]=value
    def __getitem__(self,key):
        return self._assets[key]
    def __delitem__(self,key):
        del self._assets[key]
    def __iter__(self):
        return self._assets.__iter__()
    def __len__(self):
        return len(self._assets)

class MyXMLAsset(object):
    def __init__(self):
    
        self._name=""
        self._atype=""
        self._state=""
        self._currency=""
        self._notional=0.0
        self._prepaycurve=()
        self._defaultcurve=()
        self._coupon=""
        self._carrycoupon=""
        self._maturity=""
        self._defaulttime=""
        self._calldate=()
        self._callpriced=()
        self._callfactor=()
        self._defaultrate=0.0
        self._recoveryrate=0.0
        self._recoverydelay=0.0
        self._reinvesttarget=()
        self._reinvestratio=0.0

    @prop
    def name():pass
    @prop
    def atype():pass
    @prop
    def state() :pass
    @prop
    def currency():pass
    @prop
    def notional():pass
    @prop
    def prepaycurve():pass
    @prop
    def defaultcurve():pass
    @prop
    def coupon():pass
    @prop
    def carrycoupon():pass
    @prop
    def maturity():pass
    @prop
    def defaulttime():pass
    @prop
    def calldate():pass
    @prop
    def callpriced():pass
    @prop
    def callfactor():pass
    @prop
    def defaultrate():pass
    @prop
    def recoveryrate():pass
    @prop
    def recoverydelay():pass
    @prop
    def reinvesttarget():pass
    @prop
    def reinvestratio():pass
    
class MyXMLVectors(MutableMapping):
    def __init__(self):
        self._vectors=dict()
        self._parameters=MyXMLParam()
    def __setitem__(self,key,value):
        self._vectors[key]=value
    def __getitem__(self,key):
        return self._vectors[key]
    def __delitem__(self,key):
        del self._vectors[key]
    def __iter__(self):
        return self._vectors.__iter__()
    def __len__(self):
        return len(self._vectors)
    
class MyXMLVector(MutableMapping):
    def __init__(self):
        self._pts=dict()
        self._name=""
        self._atype=""
        self._parameters=MyXMLParam()
    def __setitem__(self,index,item):
        self._pts[index]=item
    def __getitem__(self,index):
        return self._pts[index]
    def __delitem__(self,index):
        del _pts[index]
    def __len__(self):
        return len(self._pts)
    def __iter__(self):
        return self._pts.__iter__()
   
    @prop
    def name() : pass
    @prop
    def atype():pass
class MyXMLCurves(MutableMapping):
    def __init__(self):
        self._curves=dict()
        self._parameters=MyXMLParam()
    def __setitem__(self,key,value):
        self._curves[key]=value
    def __getitem__(self,key):
        return self._curves[key]
    def __delitem__(self,key):
        del self._curves[key]
    def __iter__(self):
        return self._curves.__iter__()
    def __len__(self):
        return len(self._curves)
class MyXMLCurve(object):
    def __init__(self):
        self._name=""
        self._annualized=False
        self._daycountconvention=""
        self._conditional=False
        self._vector=""
    
    @prop
    def name(): pass

    @prop
    def annualized():pass

    @prop
    def daycountconvention():pass

    @prop
    def conditional(): pass

    @prop
    def vector(): pass
class MyXMLFees(MutableMapping):
    def __init__(self):
        self._fees=dict()
        self._parameters=MyXMLParam()
    def __setitem__(self,key,value):
        self._fees[key]=value
    def __getitem__(self,key):
        return self._fees[key]
    def __delitem__(self,key):
        del self._fees[key]
    def __iter__(self):
        return self._fees.__iter__()
    def __len__(self):
        return len(self._fees)
    
class MyXMLFee(object):
    def __init__(self):
        self._name=""
        self._atype=""
        self._index=()
        self._cap=()
        self._floor=()
        self._daycountconvention=""
        self._continuous=False
        self._vector=""
    
    @prop
    def name(): pass

    @prop
    def atype() : pass

    @prop
    def index():pass

    @prop
    def daycountconvention():pass

    @prop
    def continuous(): pass

    @prop
    def vector(): pass

    @prop
    def cap() : pass

    @prop
    def floor() : pass
class MyXMLAccounts(MutableMapping):
    def __init__(self):
        self._accounts=dict()
        self._parameters=MyXMLParam()
    def __setitem__(self,key,value):
        self._accounts[key]=value
    def __getitem__(self,key):
        return self._accounts[key]
    def __delitem__(self,key):
        del self._accounts[key]
    def __iter__(self):
        return self._accounts.__iter__()
    def __len__(self):
        return len(self._accounts)


class MyXMLAccount(object):
    def __init__(self):
        self._name=""
        self._periods=()
        self._currency=""
        self._initialbalance=0.0
        self._overdraft=False
        self._carrycoupon=()

    @prop
    def name() : pass

    @prop
    def periods(): pass

    @prop
    def currency():pass

    @prop
    def initialbalance():pass

    @prop
    def overdraft(): pass

    @prop
    def carrycoupon():pass
        
class MyXMLDeal(object):
  
    def __init__(self,doc):
       grammarNode=doc.childNodes[0]
       self.data=dict()
       self._parameters=()
       self._wfs=MyXMLWaterfalls()
       self._tranches=MyXMLTranches()
       self._vectors=dict()
       self._fees=dict()
       self._cashflows=dict()
       self._NRSO=dict() #Rating Agencies
       
       
       nodeList=grammarNode.childNodes
       print len(nodeList)
       for node in nodeList:
           self.parse(node)
        
    
    def parse(self,node):
        parseMethod=getattr(self,"parse_%s" % node.__class__.__name__)
        print parseMethod
        print node.localName, node.__class__.__name__
        parseMethod(node)
        
    def parse_Document(self,node):
        print "Parsing Document"
        self.parse(node.documentElement)
    def parse_Element(self,node):
        print "Parsing Element",node.tagName
        t=()
        n=len(node.childNodes)
        print "No of child Nodes= ", n
        if n >= 1 :
            handlerMethod=getattr(self,"do_%s" % node.tagName)
            t=handlerMethod(node)
        else:
            attname="_%s" % node.tagName
            print attname,"self.%s" % node.localName
            attmethod="self.%s" % node.localName
            n=node.firstChild
            if n.nodeType==3:
                t=self.parse_Text(n)
                print "t=",t
                
           
    def parse_Comment(self,node):
        print "Parsing Comment", node.tagName
        pass
    def parse_Text(self,node):
        print "Parsing Text",node.nodeValue,node.parentNode.localName
        return node.parentNode.localName,node.nodeValue
      
    def do_parameters(self,node):
        print "Doing parameters"
        p=MyXMLParam()
        lnodeList=node.childNodes
        print len(lnodeList)
        for lnode in lnodeList:
             p[lnode.tagName]=lnode.firstChild.nodeValue
      
        self._parameters=p
      
    def do_vectors(self,node):
        print "Doing vectors"
        vlist=node.getElementsByTagName('vector')
        vectorList=MyXMLVectors()
        print len(vlist)
        for v in vlist:
            #set name and type attributes
            name=v.attributes['name'].value
            vtype=v.attributes['type'].value
            vec=MyXMLVector()
            vec._name=name
            vec._type=vtype
            #globalName[name]=vec
            plist=v.getElementsByTagName('parameters')
            #set parameters
            for p in plist:
                cns=p.childNodes
                for cn in cns:
                    vec._parameters[cn.tagName]=cn.firstChild.nodeValue
            #set values
            valList=v.getElementsByTagName('values')
           
            for valHead in valList:
                vals=valHead.childNodes
                for val in vals:
                    valIndx=int(val.attributes['index'].value)
                    valValue=val.firstChild.nodeValue
                    vec[valIndx]=valValue
                    #print valIndx,vec[valIndx]
            vectorList[name]=vec
            self._vectors[name]=vec
        globalName["vectors"]=vectorList
        pass
    def do_fees(self,node):
        print "Doing fees"
        feesList=MyXMLFees()
        vlist=node.childNodes
       
        for v in vlist:
            f=MyXMLFee()
            name=v.attributes['name'].value
            atype=v.attributes['type'].value
            
            #print name,atype
            f.name=name
            cns=v.childNodes
            for cn in cns:
                if len(cn.childNodes)==1:
                    #print cn.nodeName, cn.firstChild.nodeValue
                    setattr(f,cn.nodeName,cn.firstChild.nodeValue)
            feesList[name]=f
            #self._fees[name]=f
        globalName["fees"]=feesList
        pass
    def do_curves(self,node):
        print "Doing curves"
        curveList=MyXMLCurves()
        vlist=node.childNodes
       
        for v in vlist:
            c=MyXMLCurve()
            name=v.attributes['name'].value
            print name
            c.name=name
            cns=v.childNodes
            for cn in cns:
                print cn.nodeName, cn.firstChild.nodeValue
                setattr(c,cn.nodeName,cn.firstChild.nodeValue)
            curveList[name]=c
        globalName["curves"]=curveList
        pass
    def do_accounts(self,node):
        print "Doing accounts"
        accountList=MyXMLAccounts()
        vlist=node.childNodes
      

        for v in vlist:
            a=MyXMLAccount()
            name=v.attributes['name'].value
            
            #print name
            a.name=name
            cns=v.childNodes
            for cn in cns:
                if len(cn.childNodes)==1:
                    #print cn.nodeName, cn.firstChild.nodeValue
                    setattr(a,cn.nodeName,cn.firstChild.nodeValue)
            accountList[name]=a

        globalName["accounts"]=accountList
        pass

   
    def do_assets(self,node):
        print "Doing assets"

        assetList=MyXMLAssets()
        vlist=node.getElementsByTagName('parameters')
        
       
        for v in vlist:
            print v.tagName
            
       
        #print "parameter length=",len(vlist)
        #set parameters
        for v in vlist:
            cns=v.childNodes
            for cn in cns:
                #print cn.tagName,cn.firstChild.nodeValue
                assetList._parameters[cn.tagName]=cn.firstChild.nodeValue
    
        vlist=node.getElementsByTagName('asset')
        print "no of assets=",len(vlist)
        for v in vlist:
            a=MyXMLAsset()
            a.name=v.attributes['name'].value
            a.atype=v.attributes['type'].value
            a.state=v.attributes['state'].value
            
            #print a.name,a.atype,a.state
            cns=v.childNodes
            for cn in cns:
                if len(cn.childNodes)==1:
                    #print cn.nodeName, cn.firstChild.nodeValue
                    setattr(a,cn.nodeName,cn.firstChild.nodeValue)
           
            assetList[a.name]=a
            
        globalName["assets"]=assetList
        pass
    def do_hedges(self,node):
        print "Doing XML hedges"
        hedgeList=MyXMLHedges()
        vlist=node.getElementsByTagName('hedge')
        
       
        for v in vlist:
            print v.tagName,v.attributes['name'].value
            s=MyXMLHedge()
            s.name=v.attributes['name'].value
            s.atype=v.attributes['type'].value
            s.state=v.attributes['state'].value

            cnlist=v.getElementsByTagName('leg')
            i=0
            for cn in cnlist:
                l=MyXMLLeg()
                l.ltype=cn.attributes['type'].value
                gcnlist=cn.childNodes
                #print len(gcnlist)
                for gcn in gcnlist:
                    llist=gcn.childNodes
                    #print len(llist)
                    if len(llist)==1:
                       # print gcn.tagName,gcn.firstChild.nodeValue
                        setattr(l,gcn.tagName,gcn.firstChild.nodeValue)
                s[i]=l
                i=i+1
            hedgeList[s.name]=s
           # print len(s),i
            #print s[0].assetname,s[1].assetname
##            
        globalName["hedges"]=hedgeList

        pass
    def do_tranches(self,node):
        print "Doing tranches"
        trancheList=MyXMLTranches()
        vlist=node.getElementsByTagName('tranche')
        #print "no of tranches=",len(vlist)
       
        for v in vlist:
            #print v.tagName,v.attributes['name'].value
            t=MyXMLTranche()
            t.name=v.attributes['name'].value
            t.ttype=v.attributes['type'].value
         

            cns=v.childNodes
            for cn in cns:
                if len(cn.childNodes)==1:
                    #print cn.nodeName, cn.firstChild.nodeValue
                    setattr(t,cn.nodeName,cn.firstChild.nodeValue)
           
            trancheList[t.name]=t
        globalName["tranches"]=trancheList
        pass
    def do_variables(self,node):
        print "Doing variables"
     
        v=MyXMLParam()
        lnodeList=node.childNodes
        print len(lnodeList)
        for lnode in lnodeList:
            name=lnode.attributes['name'].value
            #print name,lnode.tagName,lnode.firstChild.nodeValue
            v[name]=lnode.firstChild.nodeValue
      
        globalName["variables"]=v
        pass
    def do_waterfall(self,node):
        print "Doing waterfall"
        wfs=MyXMLWaterfalls()
        lnodeList=node.childNodes
        wf=self.do_wf(node)
        wfs[wf.name]=wf
        globalName["waterfalls"]=wf
        pass
    
    def do_wf(self,node):
        print "Doing wf steps"
        name=node.attributes['name'].value
        wf=MyXMLWaterfall()
        i=0
        print name
        lnodeList=node.childNodes
        
        for l in lnodeList:
            print l.tagName
            if l.tagName=="waterfall":
                wf[i]=self.do_wf(l)
                i=i+1
            else:
                action=l.attributes['action'].value
                #print action
                step=MyXMLWaterfallStep()
                step.action=action
                cnlist=l.childNodes
                for cn in cnlist:
                    if len(cn.childNodes)==1:
                        print cn.tagName,cn.firstChild.nodeValue
                        setattr(step,cn.nodeName,cn.firstChild.nodeValue)
            wf[i]=step
            i=i+1
        self._wfs[name]=wf
        #globalName[name]=wf
        return wf       
    def do_cashflows(self,node):
        print "Doing cashflows"
        
        cnlist=node.childNodes

       # print len(cnlist)
        
        #cn=node.firstChild
        for cn in cnlist:
            cf=MyXMLCashFlowParams()
            gcnList=cn.childNodes
            name=cn.attributes['name'].value
            cf.name=name
            #print name
            for gcn in gcnList:
                #print gcn.nodeName
                if len(gcn.childNodes)==1:
                     setattr(cf,gcn.nodeName,gcn.firstChild.nodeValue)
                     print gcn.tagName,gcn.firstChild.nodeValue
                elif gcn.tagName=="items":
                    #print "doing items"
                    ilist=gcn.childNodes
                    #print "no items=",len(ilist)
                    for inode in ilist:
                        cfname=inode.attributes['name'].value
                        #print cfname
                        ivalueList=inode.childNodes
                        item=MyXMLCFItem()
                        item.name=cfname
                        for ivalue in ivalueList:
                            if ivalue.nodeName=="expression":
                                #print ivalue.nodeName,ivalue.firstChild.nodeValue
                                setattr(item,ivalue.nodeName,ivalue.firstChild.nodeValue)
                            elif ivalue.nodeName=="format":
                                fmt=MyXMLFormat()
                                frmtList=ivalue.childNodes
                                for frmt in frmtList:
                                    if len(frmt.childNodes)==1:
                                        #print frmt.nodeName,frmt.firstChild.nodeValue
                                        setattr(fmt,frmt.nodeName,frmt.firstChild.nodeValue)
                                item.format=fmt
                            elif ivalue.nodeName=="borders":
                                brdr=MyXMLBorders()
                                bList=ivalue.childNodes
                                for b in bList:
                                    if len(b.childNodes)==1:
                                        #print b.nodeName,b.firstChild.nodeValue
                                        setattr(brdr,b.nodeName,b.firstChild.nodeValue)
                                item.borders=brdr
                            elif ivalue.nodeValue=="font":
                                if len(ivalue.firstChild)==1:
                                    #print ivalue.nodeName,ivalue.firstChild.nodeValue
                                    setattr(item,ivalue.nodeName,ivalue.firstChild.nodeValue)
                            elif ivalue.nodeValue=="interior":
                                if len(ivalue.firstChild)==1:
                                    #print ivalue.nodeName,ivalue.firstChild.nodeValue
                                    setattr(item,ivalue.nodeName,ivalue.firstChild.nodeValue)
                        cf["cfname"]=item
            self._cashflows[name]=cf
        pass
    def do_moodys(self,node):
        print "Doing Moodys"
        m=MyXMLMoodys()
        lnodeList=node.childNodes
        #print len(lnodeList)
        for lnode in lnodeList:
            #print lnode.nodeName
            if lnode.nodeName=="parameters":
                print "doing Moodys Parameters"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        #print pnode.nodeName, pnode.firstChild.nodeValue
                        m.addparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
            elif lnode.nodeName=="vectors":
                
                print "doing Moodys vectors"
                vlist=lnode.getElementsByTagName('vector')
                #print len(vlist)
                for v in vlist:
                    #set name and type attributes
                    name=v.attributes['name'].value
                    vtype=v.attributes['type'].value
                    vec=MyXMLVector()
                    vec._name=name
                    vec._type=vtype
                    plist=v.getElementsByTagName('parameters')
                    #set parameters
                    for p in plist:
                        cns=p.childNodes
                        for cn in cns:
                            vec._parameters[cn.tagName]=cn.firstChild.nodeValue
                    #set values
                    valList=v.getElementsByTagName('values')
                   
                    for valHead in valList:
                        vals=valHead.childNodes
                        for val in vals:
                            valIndx=int(val.attributes['index'].value)
                            valValue=val.firstChild.nodeValue
                            vec[valIndx]=valValue
                    m.addvector(name,vec) 
                pass
            elif lnode.nodeName=="curves":
                print "Doing Moodys curves"
                vlist=lnode.childNodes
               
                for v in vlist:
                    c=MyXMLCurve()
                    name=v.attributes['name'].value
                    #print name
                    c.name=name
                    cns=v.childNodes
                    for cn in cns:
                        #print cn.nodeName, cn.firstChild.nodeValue
                        setattr(c,cn.nodeName,cn.firstChild.nodeValue)
                    m.addcurve(name,c)
                pass
            elif lnode.nodeName=="prepays":
                print "doing Moodys prepays"
                pplist=lnode.childNodes
                i=0
                for pp in pplist:
                    name= pp.attributes['name'].value
                    #print name
                    m.addprepay(i,name)
                    i=i+1
                pass
            elif lnode.nodeName=="scenarios":
                print "doing Moodys scenario weights"
                slist=lnode.childNodes
            
                for s in slist:
                    name= s.attributes['curve'].value
                    value=s.firstChild.nodeValue
                    #print name,value
                    m.addscenario(name,value)
                    
                pass
            elif lnode.nodeName=="shocks":
                print "doing Moodys shocks"
                slist=lnode.childNodes
            
                for s in slist:
                    name= s.attributes['value'].value
                    value=s.firstChild.nodeValue
                    #print name,value
                    m.addshock(name,value)
                pass
            elif lnode.nodeName=="ratings":
                print "doing Moodys rating table"
                
                clnodeList=lnode.childNodes
                #print len(clnodeList)
                for clnode in clnodeList:
                    rating=clnode.attributes['value'].value
                    #print rating
                    ratingtablerow=MyXMLRatingTableRow()
                    ratingtablerow.rating=rating
                    tnodeList=clnode.childNodes
                    for tnode in tnodeList:
                        year=tnode.attributes['value'].value
                        value=tnode.firstChild.nodeValue
                        ratingtablerow[year]=value
                        #print year,value
                    m.addratingrow(rating,ratingtablerow)
                pass
            elif lnode.nodeName=="cashflow":
                print "doing cashflow params"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        #print pnode.nodeName, pnode.firstChild.nodeValue
                        m.addcfparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
            elif lnode.nodeName=="outputs":
                print "doing output params"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        #print pnode.nodeName, pnode.firstChild.nodeValue
                        m.addoutputparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
            elif lnode.nodeName=="cbm":
                print "Doing CBM"
                cbm=MyXMLCBM()
                plist=lnode.childNodes
                #print len(plist)
                plist=lnode.getElementsByTagName('parameters')
                    #set parameters
                for p in plist:
                    cns=p.childNodes
                    for cn in cns:
                        #print cn.tagName,cn.firstChild.nodeValue
                        cbm.addparameter(cn.tagName,cn.firstChild.nodeValue)
                #set values
                valList=lnode.getElementsByTagName('values')
               
                for valHead in valList:
                    vals=valHead.childNodes
                    for val in vals:
                        valIndx=int(val.attributes['default'].value)
                        valValue=val.firstChild.nodeValue
                        #print valIndx,valValue
                        cbm[valIndx]=valValue
                m.setCBM(cbm) 
                pass
        self._NRSO["Moodys"]=m        
        pass
    def do_snp(self,node):
        print "Doing S&P"
      
        s=MyXMLSandP()
        lnodeList=node.childNodes
        #print len(lnodeList)
        for lnode in lnodeList:
            print lnode.nodeName
            if lnode.nodeName=="parameters":
                print "doing SandP Parameters"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        print pnode.nodeName, pnode.firstChild.nodeValue
                        s.addparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
            elif lnode.nodeName=="vectors":
                print "Doing S&P vectors"
                vlist=lnode.getElementsByTagName('vector')
                #print len(vlist)
                for v in vlist:
                    #set name and type attributes
                    name=v.attributes['name'].value
                    vtype=v.attributes['type'].value
                    print name,vtype
                    vec=MyXMLVector()
                    vec._name=name
                    vec._type=vtype
                    plist=v.getElementsByTagName('parameters')
                    #set parameters
                    for p in plist:
                        cns=p.childNodes
                        for cn in cns:
                            vec._parameters[cn.tagName]=cn.firstChild.nodeValue
                            #print cn.tagName,cn.firstChild.nodeValue
                    #set values
                    valList=v.getElementsByTagName('values')
                   
                    for valHead in valList:
                        vals=valHead.childNodes
                        for val in vals:
                            valIndx=int(val.attributes['index'].value)
                            valValue=val.firstChild.nodeValue
                            vec[valIndx]=valValue
                            #print valIndx,valValue
                    s.addvector(name,vec) 

                pass
            elif lnode.nodeName=="curves":
                print "Doing S&P curves"
                vlist=lnode.childNodes
               
                for v in vlist:
                    c=MyXMLCurve()
                    name=v.attributes['name'].value
                    print name
                    c.name=name
                    cns=v.childNodes
                    for cn in cns:
                        print cn.nodeName, cn.firstChild.nodeValue
                        setattr(c,cn.nodeName,cn.firstChild.nodeValue)
                    s.addcurve(name,c)
                pass
            elif lnode.nodeName=="desiredratings":
                print "Doing S&P desiredratings"
                vlist=lnode.childNodes
                for v in vlist:
                    name=v.attributes['name'].value
                    value=v.firstChild.nodeValue
                    print name,value
                    s.adddesiredrating(name,value)
                pass
            elif lnode.nodeName=="prepays":
                print "Doing S&P Prepays"
                pplist=lnode.childNodes
                i=0
                for pp in pplist:
                    name= pp.attributes['name'].value
                    print name
                    s.addprepay(i,name)
                    i=i+1
                pass
            elif lnode.nodeName=="defaults":
                print "Doing S&P Defaults"
                snlist=lnode.childNodes
                i=0
                for sn in snlist:
                    name= sn.attributes['name'].value
                    print i,name
                    s.addscenario(i,name)
                    i=i+1
                pass
            elif lnode.nodeName=="recoveryrates":
                print "Doing S&P recovery rates"
                snlist=lnode.childNodes
                
                i=0
                for sn in snlist:
                    name=sn.attributes['name'].value
                    dly=sn.attributes['delay'].value
                    spRR=SandP_RR()
                    value=sn.firstChild.nodeValue
                    print name,dly,value
                    spRR.name=name
                    spRR.delay=dly
                    spRR.rr=value
                    
                    s.addRR(name,spRR)
                pass
            elif lnode.nodeName=="hurdlerates":
                print "Doing S&P hurdle rates"
                snlist=lnode.childNodes
                
                i=0
                for sn in snlist:
                    name=sn.attributes['name'].value
                    
                    value=sn.firstChild.nodeValue
                    print name,value
                    
                    s.addhurdlerate(name,value)
                pass
            elif lnode.nodeName=="cashflow":
                print "Doing S&P cashflow"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        print pnode.nodeName, pnode.firstChild.nodeValue
                        s.addcfparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
            elif lnode.nodeName=="outputs":
                print "Doing S&P outputs"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        print pnode.nodeName, pnode.firstChild.nodeValue
                        s.addoutputparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass

        self._NRSO["SandP"]=s 
        pass
    def do_fitch(self,node):
        print "Doing Fitch"
        
      
        f=MyXMLFitch()
        lnodeList=node.childNodes
        #print len(lnodeList)
        for lnode in lnodeList:
            print lnode.nodeName
            if lnode.nodeName=="parameters":
                print "doing Fitch Parameters"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        print pnode.nodeName, pnode.firstChild.nodeValue
                        f.addparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
            elif lnode.nodeName=="vectors":
                print "Doing Fitch vectors"
                vlist=lnode.getElementsByTagName('vector')
                #print len(vlist)
                for v in vlist:
                    #set name and type attributes
                    name=v.attributes['name'].value
                    vtype=v.attributes['type'].value
                    print name,vtype
                    vec=MyXMLVector()
                    vec._name=name
                    vec._type=vtype
                    plist=v.getElementsByTagName('parameters')
                    #set parameters
                    for p in plist:
                        cns=p.childNodes
                        for cn in cns:
                            vec._parameters[cn.tagName]=cn.firstChild.nodeValue
                            #print cn.tagName,cn.firstChild.nodeValue
                    #set values
                    valList=v.getElementsByTagName('values')
                   
                    for valHead in valList:
                        vals=valHead.childNodes
                        for val in vals:
                            valIndx=int(val.attributes['index'].value)
                            valValue=val.firstChild.nodeValue
                            vec[valIndx]=valValue
                            #print valIndx,valValue
                    f.addvector(name,vec) 

                pass
            elif lnode.nodeName=="curves":
                print "Doing Fitch curves"
                vlist=lnode.childNodes
               
                for v in vlist:
                    c=MyXMLCurve()
                    name=v.attributes['name'].value
                    print name
                    c.name=name
                    cns=v.childNodes
                    for cn in cns:
                        print cn.nodeName, cn.firstChild.nodeValue
                        setattr(c,cn.nodeName,cn.firstChild.nodeValue)
                    f.addcurve(name,c)
                pass
            elif lnode.nodeName=="desiredratings":
                print "Doing Fitch desiredratings"
                vlist=lnode.childNodes
                for v in vlist:
                    name=v.attributes['name'].value
                    value=v.firstChild.nodeValue
                    print name,value
                    f.adddesiredrating(name,value)
                pass
            elif lnode.nodeName=="prepays":
                print "Doing Fitch Prepays"
                pplist=lnode.childNodes
                i=0
                for pp in pplist:
                    name= pp.attributes['name'].value
                    print name
                    f.addprepay(i,name)
                    i=i+1
                pass
            elif lnode.nodeName=="defaults":
                print "Doing Fitch Defaults"
                snlist=lnode.childNodes
                i=0
                for sn in snlist:
                    name= sn.attributes['name'].value
                    print i,name
                    f.addscenario(i,name)
                    i=i+1
                pass
            elif lnode.nodeName=="recoveryrates":
                print "Doing Fitch recovery rates"
                snlist=lnode.childNodes
                
                i=0
                for sn in snlist:
                    name=sn.attributes['name'].value
                    dly=sn.attributes['delay'].value
                    fRR=Fitch_RR()
                    value=sn.firstChild.nodeValue
                    print name,dly,value
                    fRR.name=name
                    fRR.delay=dly
                    fRR.rr=value
                    
                    f.addRR(name,fRR)
                pass
            elif lnode.nodeName=="hurdlerates":
                print "Doing Fitch hurdle rates"
                snlist=lnode.childNodes
                
                i=0
                for sn in snlist:
                    name=sn.attributes['name'].value
                    
                    value=sn.firstChild.nodeValue
                    print name,value
                    
                    f.addhurdlerate(name,value)
                pass
            elif lnode.nodeName=="cashflow":
                print "Doing Fitch cashflow"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        print pnode.nodeName, pnode.firstChild.nodeValue
                        f.addcfparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
            elif lnode.nodeName=="outputs":
                print "Doing Fitch outputs"
                plist=lnode.childNodes
                for pnode in plist:
                    if len(pnode.firstChild)>1:
                        print pnode.nodeName, pnode.firstChild.nodeValue
                        f.addoutputparameter(pnode.nodeName,pnode.firstChild.nodeValue)
                pass
        self._NRSO["Fitch"]=f 
        pass
    def do_analytics(self,node):
        print "Doing analytics"
        # not interest in this node for now
        pass
    

def test():
    print "Start"
    xmldoc=minidom.parse("deal2.xml")
    #print xmldoc.toxml()
    k=MyXMLDeal(xmldoc)
    print "Global Objects, no=",len(globalName)
    for k in globalName.keys():
        print k




