from cdoconfig import globalName
from datetime import date
import MyCDOXML
from myInstrument import MyInstrument
from myInstrument import MyAsset
from myInstrument import MyTranche
from myInstrument import MyDayCount
from myInstrument import MyAccount
from myInstrument import MyFee
from myInstrument import MyCurve
from myInstrument import MyHedge
from myInstrument import MyHedgeLeg
import myschedule
import MYCDO
from MYCDO import MyWaterfallStep
from MYCDO import MyWaterfall
from myschedule import MySchedulePt
MyCDOXML.test()
AssetPool=dict()

def makeschedule(dates,values):
    schedule=list()
    print (len(dates),len(values))
    diter=iter(dates)
    viter=iter(values)
    try:
        while True:
            d=diter.next()
            v=viter.next()
            #print dates[d],values[v]
            p=MySchedulePt(dates[d],values[v])
            schedule.append(p)
    except StopIteration:
        pass
    return schedule

def createdates(xmlvec):
    schedule=list()
     
    for v in xmlvec:
        
        d=xmlvec[v]
            
        if isinstance(d,unicode):
            d1=date(1900,1,1)
            d1=d1.fromordinal(d1.toordinal()+int(d)-2)
                
        else:
                d1=d
        p=MySchedulePt(d1,0.0)
        schedule.append(p)
    return schedule

igN=iter(globalName)
while True:
    try:
        key=igN.next()
        print (key, globalName[key])
    except StopIteration:
        break



    
def buildFromXML():

    print ("================= Doing Vectors ===========================")
    vectorList=globalName["vectors"]
    print (len(vectorList))
    print (type(vectorList))
    vectors=dict()
    for vn in vectorList:
        vl=vectorList[vn]
        print ("Vector", vl.name, type(vl))
        vec=dict()
        ivl=iter(vl)
        try:
            while True:
                i=ivl.next()
                #print i,vl[i]
                vec[i]=vl[i]
        except StopIteration:
            pass
        vectors[vl.name]=vec

    pd=vectors["DealPeriods"]
    print ("Deal periods",len(pd))
    ipd=iter(pd)
    try:
        while True:
            i=ipd.next()
            print (i,pd[i])
    except StopIteration:
        pass
    exit
    print( "================= Doing Curves ============================")
    curveList=globalName["curves"]
    print (len(curveList))
    print (type(curveList))
    curves=dict()
    for cn in curveList:
        cv=curveList[cn]
        print ("Curve", cv.name,cv.vector)
        curve=MyCurve()

        curve.name=cv.name
        curve.annualized=cv.annualized
        curve.conditional=cv.conditional
        curve.dc.setType(cv.daycountconvention)
        curve.rates=vectors[cv.vector]
        curves[curve.name]=curve
    print( "================= Doing Fees===============================")
    feeList=globalName["fees"]
    print (len(feeList))
    print (type(feeList))
    fees=dict()
    for fn in feeList:
        fl=feeList[fn]
        print ("Fee", fl.name, type(fl),fl.vector)
        fee=MyFee()
        fee.name=fl.name
        fee.ftype=fl.atype
        fee.dc.setType(fl.daycountconvention)
        fee.floor=fl.floor
        fee.cap=fl.cap
        fee.rates=vectors[fl.vector]
        fees[fee.name]=fee

    print (fees["SwapFltgCoupon1"].rates)
    print ("================= Doing Assets ============================")

    assetList=globalName["assets"]
    print (len(assetList))
    print( type(assetList))
    assets=dict()
    for an in assetList:
        al=assetList[an]
        print ("Asset",al.name, type(al))
        asset=MyAsset()

        asset.currency=al.currency
        asset.state=al.state
        asset.name=al.name
        asset.setschedule(pd)

        cpn=al.coupon
        print (al.coupon, type(al.coupon))
        print ("Coupon",al.coupon)
        fee=fees[al.coupon]
        print ("Fee name",fee.name)
        print ("Day Count",fee.dc)
        daycount=MyDayCount()
        daycount.dc=fee.dc
        print (daycount)
        asset.setDC(daycount)
        #vec=vectors[fee.vector]
        vec=fee.rates
        #print vec.name, len(vec),type(vec)
        v=dict()
        vecitr=iter(vec)
        i=0
        while True:
            try:
                i=vecitr.next()
                val=vec[i]
                print (i,val)
                v[i]=val

            except StopIteration:
                break
        if  fee.index != None:
            print (" Fee Index=",fee.index)
            indx=vectors[fee.index]
            ndx=makeschedule(pd,indx)
            asset.setCurve(ndx)

        else:
            indx=None
            ndx=None
            print ("No index")
        print ("v ",type(v),len(v))
        asset.setCoupn(fee,v,ndx)




        asset.nominal=float(al.notional)
        if al.prepaycurve != ():
            print ("Prepay Curve=",al.prepaycurve)
            amortcrv=curves[al.prepaycurve]
            amortrates=amortcrv.rates
    ##        if amortcrv.vector != ():
    ##            amortrates=curves[amortcrv.vector]
    ##            print "Amortising Rates =", amortcrv.name,amortrates,len(amortrates)
    ##            dp=amortrates._parameters["periods"]

            periods=pd
            asset.buildamort(periods,amortrates)
            asset.buildCFs()

        assets[asset.name]=asset

    print ("No of assets=",len(assets))
    for ia in assets:
        print (ia)
    print( "====================Doing Tranches==============================")
    trancheList=globalName["tranches"]
    print ("No of tranches",len(trancheList),type(trancheList))
    tranches=list()
    for t in trancheList:
        tr=trancheList[t]
        tranche=MyTranche()
        print (type(tr), tr.name)
        tranche.name=tr.name
        tranche.nominal=float(tr.notional)
        print ("Coupon",tr.coupon)
        fee=fees[tr.coupon]

        print ("Fee name",fee.name)

        print ("Day Count",fee.dc)
        #tranche.setDC(fee.daycountconvention)
        #vec=vectors[fee.rates]
        vec=fee.rates
        xmlfees=globalName["fees"]
        xmlvectors=globalName["vectors"]

        xmlfee=xmlfees[fee.name]
        xmlvec=xmlvectors[xmlfee.index]
        print (xmlvec.name,len(xmlvec),len(vec))

        dpname=xmlvec._parameters["periods"]
        print( "periods=",dpname)
        dp=xmlvectors[dpname]

        tranche.setschedule(dp)

        vecitr=iter(vec)
        i=0
        while True:
            try:
                i=vecitr.next()
                val=vec[i]
                print (i,val)
                v[i]=val

            except StopIteration:
                break


        if fee.index != None:
            print( " Fee Index=",fee.index)
            indx=vectors[fee.index]
            ndx=makeschedule(pd,indx)
            tranche.setCurve(ndx)

        else:
            indx=None
            ndx=None
            print( "No index")
        print ("v ",type(v),len(v))
        tranche.setCoupn(fee,v,ndx)
        tranche.buildCFs()
        tranches.append(tranche)
    print ("====================Doing Accounts ==============================")
    acctList=globalName["accounts"]
    accounts=list()
    print ("No of accounts",len(acctList),type(acctList))
    for a in acctList:
        acct=acctList[a]
        periodName=acct.periods
        dp=vectors[periodName]
        periods=createdates(dp)

        print (type(acct), acct.name,acct.initialbalance,periodName)
        ob=float(acct.initialbalance)
        account=MyAccount(periods,ob)
        account.name=acct.name
        account.init_balances(periods,ob)

        accounts.append(account)
    print ("===================== Doing Hedges ==================================")
    XMLhedgeList=globalName["hedges"]
    hedges=list()
    print ("No of hedges",len(XMLhedgeList),type(XMLhedgeList))
    for h in XMLhedgeList:
        XMLhdge=XMLhedgeList[h]

        print (type(XMLhdge), XMLhdge.name,XMLhdge.stype,XMLhdge.state,len(XMLhdge))
        hedge=MyHedge()
        hedge.name=XMLhdge.name
        hedge.htype=XMLhdge.stype
        hedge.state=XMLhdge.state

        ih=iter(XMLhdge)
        while True:
            try:
                l=ih.next()
                XMLleg=XMLhdge[l]
                print (l,XMLleg.ltype, XMLleg.assetname)
                leg=MyHedgeLeg()
                leg.ltype=XMLleg.ltype
                asst=assets[XMLleg.assetname]
                leg.addAsset(XMLleg.assetname,asst)
                hedge.addLeg(leg)
            except StopIteration:
                break
        hedges.append(hedge)

    print ("===================== Doing Waterfalls ==============================")
    def printWFActions(XMLwf):
        print ("length of WF",len(XMLwf))
        for i in XMLwf:
            XMLStep=XMLwf[i]

            if isinstance(XMLStep,MyCDOXML.MyXMLWaterfall):
                print (XMLStep.name, "length=",len(XMLStep))
                printWFActions(XMLStep)
            elif isinstance(XMLStep,MyCDOXML.MyXMLWaterfallStep):
                print (i,"action=",XMLStep.action," from ",XMLStep.payable," to", XMLStep.receivable)
    def buildWFActions(XMLwf,wf):

        print ("length of WF",len(XMLwf),XMLwf.name)
        j=0
        for i in XMLwf:
            XMLStep=XMLwf[i]

            if isinstance(XMLStep,MyCDOXML.MyXMLWaterfall):
                print (XMLStep.name, "length=",len(XMLStep))
                newWF=MyWaterfall()
                buildWFActions(XMLStep,newWF)
                wf[j]=newWF
            elif isinstance(XMLStep,MyCDOXML.MyXMLWaterfallStep):
                print (i,"action=",XMLStep.action," from ",XMLStep.payable," to", XMLStep.receivable)
                step=MyWaterfallStep()
                step.action=XMLStep.action
                step.logic=XMLStep.logic
                step.condition=XMLStep.condition
                step.payable=XMLStep.payable
                step.receivable=XMLStep.receivable
                step.amount=XMLStep.amount
                step.cap=XMLStep.cap
                wf[j]=step
            j=j+1
    XMLwfList=globalName["waterfalls"]
    wfs=list()
    wf=MyWaterfall()
    #printWFActions(XMLwfList)
    buildWFActions(XMLwfList,wf)

print ("Building from XML")
buildFromXML()