##======================================================================
## Version 1.1
## Instrument and Tranches Library
## Darren Smith c 2011
#
##=======================================================================

from datetime import timedelta
from datetime import date
from myschedule import MyScheduleGenerator
from myschedule import MySchedulePt
from collections import MutableMapping

import sys
import re
from cdoconfig import prop

import MyCDOXML
##================================================================
## Class Enum
## Purpose: emulates a closed set of enumerated values
## Used by : CouponType and DayCount
##
##================================================================
class Enum(set):
    def __getattr__(self,name):
        if name in self:
            return name
        raise AttributeError
##================================================================
## Class CouponType
## Purpose: An child of Enum which is used to set coupon type
## Used by : CouponType and DayCount
##
##================================================================

class MyCouponType(Enum):

    # Class to denote different rate payments
    # types include Fixed,Floating,Variable,Other
    types=Enum(['Fixed','Floating','Variable','Other'])
    def __init__(self):
            self._typ=MyCouponType.types.Floating

           
    def setType(self,t):
            if t in MyCoupon.types:
                self.typ=t
            else:
                raise AttributeError
                
    @prop
    def typ():pass
    
    def getType(self):
            return self.typ
   
    def __str__(self):
           return self.typ
##================================================================
## Class Flow
## Purpose: A generic record used to record cash-flows
## Used by : Instrument, Account
## Parent : object
## Children : TrancheFlow
##
##================================================================

class MyFlow(object):
        def __init__(self):
                self.pd=date.today()
                self.opening_balance=0.0
                self.closing_balance=0.0
                self.interest=0.0
                self.principal=0.0
                self.default=0.0
                self.assrecovery=0.0
                self.recovery=0.0
                self.prepay=0.0
        def setFlow(self,d,ob,cb,i,p,df,r,ar,pp):
                 self.pd=d
                 self.opening_balance=ob
                 self.principal=p
                 self.interest=i
                 self.default=df
                 self.recovery=r
                 self.assrecovery=ar
                 self.prepay=pp
                 self.closing_balance=ob-self.principal-self.default-self.prepay
        def __str__(self):
                rep=str(self.pd)
                rep += ", "+ str(self.opening_balance) +", "
                rep += str(self.principal) +", "
                rep += str(self.interest) + ", "
                rep += str(self.default) + ", "
                rep += str(self.recovery) + ", "
                rep += str(self.assrecovery)+ ", "
                rep += str(self.prepay) + ", "
                rep += str(self.closing_balance)
                return rep
        def __repr__(self):
                rep=str(self.pd)
                rep += ", "+ str(self.opening_balance) +", "
                rep += str(self.principal) +", "
                rep += str(self.interest) + ", "
                rep += str(self.default) + ", "
                rep += str(self.recovery) + ", "
                rep += str(self.assrecovery)+ ", "
                rep += str(self.prepay) + ", "
                rep += str(self.closing_balance)
                return rep

        def getPD(self):
                return self.pd
        def getOB(self):
                return self.opening_balance
        def getCB(self):
                return self.closing_balance
        def getI(self):
                return self.interest
        def getP(self):
                return self.principal
        def getDef(self):
                return self.default
        def getRec(self):
                return self.recovery
        def getPP(self):
                return self.prepay
        def getAssumedRec(self):
                return self.assumedrec

        def setPD(self,payd):
                 self.pd=payd
        def setOB(self,ob):
                self.opening_balance=ob
        def setCB(self,cb):
                self.closing_balance=cb
        def setI(self,i):
                 self.interest=i
        def setP(self,p):
                 self.principal=p
        def setDef(self,df):
                 self.default=df
        def setRec(self,rec):
                self.recovery=rec
        def setPP(self,pp):
                self.prepay=pp
        def setAssumedRec(self,assrec):
               self.assrecovery=assrec
##================================================================
## Class TrancheFlow
## Purpose  : A generic record used to record cash-flows
## Used by  : Tranche
## Parent   : Flow
## Children : none
## Comments: Main difference is the distinction of due and paid interest
##           need add PIK flag and allow for PIK'
##
##================================================================
class MyTrancheFlow(MyFlow):
        def __init__(self):
            self.interestdue=0.0
            self.interestpastdue=0.0
        def setInterestDue(self,id):
            self.interestdue=id
        def setInterestPastDue(self,pd):
            self.interestpastdue=0.0
        def getInterestDue(self):
            return self.interestdue
        def getInterestPastDue(self):
            return self.interestpastdue
        def setFlow(self,d,ob,cb,i,p,df,r,ar,pp,intDue,intPDue):
            super(MyTrancheFlow,self).setFlow(d,ob,cb,i,p,df,r,ar,pp)
            self.interestdue=intDue
            self.interestpastdue=intPDue
            
        def __repr__(self):
            retval=MyFlow.__repr__(self)
            retval+=", "+self.interestdue+", "+ self.interestpastdue
            return retval
        def __str__(self):
            retval=MyFlow.__str__(self)
            retval+=", "+self.interestdue+", "+ self.interestpastdue
            return retval
##================================================================
## Class DayCount
## Purpose  : An enumerated type to distinguish accrual types
## Used by  : Instrument,Tranche
## Parent   : object 
## Children : none
## Comments : Should it be a child of Enum?
##           
##
##================================================================ 
class MyDayCount(object):
        # Class to calculate difference in accruals
        # types include A/360, 30/360E, 30/360, Act/365,Act/Act
        types=Enum(['ACT360','D30360','D30360E','ACT365','ACTACT'])
        def __init__(self):
                self._typ=MyDayCount.types.ACT360
                self.diy=360.0
               
        def convertType(self,t):
            if t.rfind("/") != -1:
               
                s=t.replace("/","")    
            else:
                s=t
            return s
        def setType(self,t):
            
                tdash=self.convertType(t)
                print tdash
                if tdash == "30360" or tdash == "30360E":
                    tdash="D"+tdash
                    print tdash
                if tdash in MyDayCount.types:
                    self.typ=tdash
                    if self.typ==MyDayCount.types.ACT365 or self.typ==MyDayCount.types.ACTACT:
                       self.diy=365.0
                    else:
                        self.diy=360.0
                else:
                    raise AttributeError
                    

        def getType(self):
                return self.typ
       
        def __str__(self):
               return self.typ
        @prop
        def typ(): pass
        def diffdays(self,d1,d2):
            difference=0
            if self.typ==MyDayCount.types.ACT360 or\
            self.typ==MyDayCount.types.ACTACT or\
            self.typ==MyDayCount.types.ACT365:
                difference=d2.toordinal()-d1.toordinal()
            elif self.typ==MyDayCount.types.D30360 or self.typ==MyDayCount.types.D30360E:
                day1=d1.day
                day2=d2.day
                mth1=d1.month
                mth2=d2.month
                if day1>30:
                    day1=30
                if day2>30 and self.typ==MyDayCount.types.D30360 and day1<30:
                    day2=1
                    mth2=mth2+1
                elif day2>30:
                    day2=30

    
                yr1=d1.year
                yr2=d2.year

                difference=(yr2-yr1)*360
                difference+=(mth2-mth1)*30
                difference+=(day2-day1)
                
            return difference
        def accrual(self,d1,d2):
            acc=(self.diffdays(d1,d2)/self.diy)
            return acc
##================================================================
## Class MyInstrument
## Purpose  : A class to generate instrument cashflows
## Version  : 1.0
## Used by  : Holding
## Parent   : object
## Children : Tranche,Asset
## Comments: Need to factor out coupon also factor out amortization profile
##           
##
##================================================================                 
class MyInstrument(object):
        def __init__(self):
                self._name=""
                print "in my Instrument init"
                self._frq=4
                #self._cpn=0.025
                self._coupon=MyCoupon()
                #self.cpnType="floating"
                self._adjust=True
                self._sd=date.today()
                self._yr=self.sd.year+10
                self._md=self.sd.replace(year=self.yr)
                self._index=0.04
                self._nominal=10e6
                self._factor=1
                self._schedule=list()
                self._payday=self.sd.day # payment day
                self._amprofile=list()
                self._cfs=list()
                self._dc=MyDayCount()
                #self._crv=list()
                self._defrate=0.0
                self._defschedule=list()
                self._recrate=0.5
                self._recdelay=4
                self._assrecrate=0.6
                self._prepay=0.0
                
            
        @prop
        def name():pass
        @prop
        def frq():pass
##        @prop
##        def cpn():pass
        @prop
        def adjust():pass
        @prop
        def sd():pass
        @prop
        def yr():pass
        @prop
        def md():pass
        @prop
        def index():pass
        @prop
        def nominal():pass
        @prop
        def factor():pass
        @prop
        def schedule():pass
        @prop
        def payday():pass
        @prop
        def amprofile():pass
        @prop
        def cfs():pass
        @prop
        def dc():pass
        @prop
        def crv():pass
        @prop
        def defrate():pass
        @prop
        def defschedule():pass
        @prop
        def recrate():pass
        @prop
        def recdelay():pass
        @prop
        def assrecrate():pass
        @prop
        def prepay():pass
        
        
        def setAdjust(self,torf):
            self.adjust=torf
        def getAdjust(self):
            return self.adjust
        def getName(self):
            return self.name
        def setName(self,n):
            self.name=n
       
        def getCpn(self):
                return self.cpn
        def setCpn(self,c):
                self._coupon.rates=c
        def setCoupn(self,dc,rates,indx=None):
            if indx!=None:
                #print indx
                self._coupon.ctype="Floating"
                self.cpnType="floating"
                self.index=indx
                #print self.__dict__
                #super(MyInstrument,self).setCurve(indx)
                self._coupon.index=indx
                self._coupon.rates=rates
                print dc
                self._coupon.daycount.setType(dc)
                self.dc.setType(dc)
            else:
                self._coupon.ctype="Fixed"
                self.cpnType="fixed"
            print self    
            self._coupon.rates=rates
           
            if isinstance(rates,list) or isinstance(rates,dict):
                print "length rates=",len(rates)
                print "cpn rate/spread= ",rates[0]
            else:
                print "cpn rate/spread= ",rates
            pass

        def getFrq(self):
            return self.frq
        def setFrq(self,f):
                self.frq=f
        def getCpnType(self):
                return self.cpnType
        def setCpnType(self,ct):
                self.cpnType=ct
        def getSD(self):
                return self.sd
        def setSD(self,d):
                self.sd=d
        def getMD(self):
                return self.md
        def setMD(self,d):
                self.md=d
        def getNdx(self):
                return self.index
        def setNdx(self,ndx):
                self.index=ndx
        def getNotional(self):
                return self.nominal
        def setNotional(self,n):
                self.nominal=n
        def getfactor(self):
                return self.factor
        def setfactor(self,f):
                self.factor=f
        def getschedule(self):
                return self.schedule
        def setschedule(self,s):
                self._schedule=s
        def setPayDay(self,d):
                self.payday=d
        def getPayDay(self):
                return self.payday
        def setDC(self,dc):
            self.dc=dc
        def getDC(self):
            return dc
        def setPrePay(self,pp):
            if pp > 1.0:
                print "Excessive prepayrate"
            self.prepay=pp
        def getPrePay(self):
            return self.prepay
        def setCurve(self,crv):
            self.curve=crv
        def setAmortization(self,ams):
            self.amprofile=ams
        def setDefRate(self,d):
            self.defrate=d
        def setDefSchedule(self,ds):
            self.defschedule=ds
        def getDefRate(self):
            return self.defrate
        def getDefSchedule(self):
            return self.defschedule
        def setRecRate(self,rr):
            self.recrate=rr
        def setAssumedRecRate(self,rr):
            self.assrecrate=rr
        def setRecDelay(self,rd):
            self.recdelay=rd
        def getRecRate(self):
            return self.recrate
        def getAssumedRecRate(self):
            return self.assrecrate
        def getRecDelay(self):
            return self.recdelay
            
        def generateSchedule(self):
                s=MyScheduleGenerator()
                s.frq=self.frq
                s.sd=self.sd
                s.md=self.md
                s.payday=self.payday
                s.doAdjust=self.adjust
                self.schedule=s.generate()
        def getNumPayments(self):
                return len(self.schedule)

##        def getCurve(self):
##            return self.curve
        def readAmProfile(self,fname):
                f=open(fname,'r')
                p=re.compile('%')
                
                for line in f:
                        g=p.split(line)
                        self.amprofile.append(round(float(g[0]),4))

        def payInterest(self,d1,d2,notional,c):
            
            if isinstance(c,unicode):
                c=float(c)
            return self.dc.accrual(d1,d2)*notional*c
        def getPeriodRate(self,i):
            if self.cpnType=="floating":
                indx=icrv[i].value
                c=indx+self.cpn
            else:
                c=self.cpn
        def calcInterestDue(self,cpn,amnt,d1,d2):
            return self.dc.accrual(d1,d2)*amnt*cpn
        def buildCFs(self):
                i=1
                self.cfs=list()
                print len(self._amprofile)
                iam=iter(self._amprofile)
                isch=iter(self._schedule)
                d1=isch.next().date
                #print "D1=",d1
                am=iam.next()
##                if self.cpnType=="floating":
##                    print "Curve=",self._crv
##                    icrv=iter(self._crv)
                    
##                    try: 
##                        indx=icrv.next().value
##                    except StopIteration:
##                        print "crv error"
##                        print self._crv
##                        exit
                
                while True:
                        try:
                            am=(iam.next()).value
                            am=float(am)
                            c=self._coupon.getPeriodRate(i)
                            #print "am=",am,float(am),type(am)
                            
##                            if self._coupon.cpnType=="floating":
##                                indx=icrv.next().value
##                                print "indx=",indx
##                                c=indx+self.cpn
##                            else:
##                                c=self.cpn
##                            print "coupn=",c,self.cpn
                            d2=isch.next().date
                            
                            
                            
                            prin=self.nominal*am
                            
                            if i==1:
                                ob=self.nominal
                            else:
                                ob=cb
                            cb=ob-prin
                            
                            #print "d1,d2=",d1,d2
                            intrst=self.payInterest(d1,d2,ob,c)
                            cf=MyFlow()
                            i=i+1
                            cf.setFlow(d2,ob,cb,intrst,prin,0.0,0.0,0.0,0.0)
                            self.cfs.append(cf)
                            d1=d2
                        except StopIteration:
                            print "curve error, iteration i=",i
                            break
        def resetPayDates(self):
            # used to calculate payment dates that do not adjust but are paid later
            icf=iter(self.cfs)
            sg=MyScheduleGenerator()
            while not(self.adjust):
                try:
                    flow=icf.next()
                    flow.pd=sg.adjust(flow.pd)
                except StopIteration:
                    break
                
        def updateCFs(self):
            i=0
            self.cfs=list()
            iam=iter(self._amprofile)
            isch=iter(self._schedule)
            d1=isch.next().date
        
            am=iam.next()
            
##            if self.cpnType=="floating":
##                icrv=iter(self.crv)
##                indx=icrv.next().value
            idefr=iter(self.defschedule)
         
            assrecAmt=0.0
            recAmt=0.0
            prepayAmt=0.0
            totalPPAmt=0.0
            totalPrin=0.0
            totaldefAmt=0.0
            totalampct=0.0
            adjustedampct=0.0
            while True:
                    try:
                        am=(iam.next()).value
##                        if self.ctype=="floating":
##                            
##                            #indx=icrv.next().value
##                            #c=indx+self.cpn
##                        else:
##                            c=self.cpn
                        c=self._coupon.getPeriodRate(i)
                        d2=isch.next().date
                        try:
                            default=idefr.next()
                        except StopIteration:
                            default=0.0
                            pass
                        defAmount=default*self.nominal*self.defrate
                        assrecAmt=assrecAmt+defAmount*self.assrecrate
                        #recAmt=defAmount*self.recrate
                        assert totalampct<1.0
                        adjustedampct=am/(1.0-totalampct)
                        #print "totalampct=", totalampct, "adjustedampct=", adjustedampct
                        totalampct=totalampct+am
                        
                        totaldefAmt=totaldefAmt+defAmount
                        
                   
                       
                        if i==0:
                            ob=self.nominal
                            assumedrec=0
                        else:
                            ob=cb
                            assumedrec=self.cfs[i-1].assrecovery+assrecAmt

                        prin=(ob-defAmount)*adjustedampct
                        totalPrin=totalPrin+prin
                        
                        prepayAmt=(self.nominal-totalPrin-totaldefAmt-totalPPAmt)*self.prepay/self.frq
                        cb=ob-prin-defAmount-prepayAmt
                        totalPPAmt=totalPPAmt+prepayAmt
                        
                        intrst=self.payInterest(d1,d2,ob,c)
                        cf=MyFlow()
                        
                        if i-self.recdelay>=0:
                            recAmt=self.cfs[i-self.recdelay].default*self.recrate
                            assrecAmt=assrecAmt-recAmt*self.assrecrate/self.recrate
                        else:
                            rec=0
                        cf.setFlow(d2,ob,cb,intrst,prin,defAmount,recAmt,assrecAmt,prepayAmt)
                        
                        self.cfs.append(cf)
                        i=i+1
                        d1=d2
                    except StopIteration:
                        break
        def deepCopy(self,instr):
            self.name=instr.name
            self.frq=instr.frq
            #self.cpn=instr.cpn
            #self.cpnType=instr.cpnType
            self.adjust=instr.adjust
            self.sd=instr.sd
            self.md=instr.md
            #self.index=instr.index
            self.nominal=instr.nominal
            self.factor=instr.factor
            self.schedule=list()
            self.payday=instr.payday
            self.amprofile=instr.amprofile
            self.cfs=list()
            #self.dc=MyDayCount()
            #self.crv=list()
            self.defrate=0.0
            self.defschedule=list()
            self.recrate=0.5
            self.recdelay=4
            self.assrecrate=0.6
            self.prepay=0.0
        def __str__(self):
            return str(self.name)#", "+ str(self.cpn)+", "+str(self.cpnType)
##================================================================
## Class MyCoupon
## Purpose  : A class to generate instrument cashflows
## Version  : 1.0
## Used by  : MyAsset
## Parent   : object
## Children : 
## Comments: Need to incorporate in MyInstrument
##           
##
##================================================================               
class MyCoupon(object):
    def __init__(self):
        self._ctype=MyCouponType()
        self._daycount=MyDayCount()
        self._cap=""
        self._floor=""
        self._index=list()
        self._rates=list()
    @prop
    def ctype():pass
    @prop
    def daycount():pass
    @prop
    def cap():pass
    @prop
    def floor():pass
    @prop
    def index():pass
    @prop
    def rates():pass
    def getPeriodRate(self,i):
      
        if isinstance(self._rates,list) or isinstance(self._rates,dict):
            if len(self._rates)<=i:
                spread=float(self._rates[len(self._rates)-1])
            else:
                spread=float(self._rates[i])
        else:
            spread=self._rates
        if self.ctype=="Floating":
            c=float(self._index[i].value)+spread
            print "i=",i,"c=",c,"index=",self._index[i].value,"spread=",spread
        else:
            c=float(spread)
        return c
   
        
            
   
##================================================================
## Class Asset
## Purpose  : A class to hold asset flows
## Version  : 1.0
## Used by  : 
## Parent   : Instrument
## Children : 
## Comments: need to factor out coupon type
##           
##================================================================          

class MyAsset(MyInstrument):
    def __init__(self):
        
        self._atype=""
        self._state=""
        self._currency=""
        self._coupon=MyCoupon()
        print "In My Asset init"
        
        super(MyAsset,self).__init__()

    def setCoupn(self,coupon,rates,indx=None):
        if indx!=None:
            
            self._coupon.ctype="Floating"
            self.cpnType="floating"
            self.index=indx
            
            self._coupon.index=indx
            self._coupon.rates=rates
            print coupon.daycountconvention
            self._coupon.daycount.setType(coupon.daycountconvention)
            self.dc.setType(coupon.daycountconvention)
        else:
            self._coupon.ctype="Fixed"
            self.cpnType="fixed"
        print self    
        self._coupon.rates=rates
       
        print "cpn rate/spread= ",rates[0]
        pass
    def buildamort(self,payDates,pct):
        print len(payDates),len(pct)
       
        diter=payDates.itervalues()
        piter=pct.itervalues()
        while True:
            try:
                d=diter.next()
                v=piter.next()
           
                pt=MySchedulePt(d,v)
                
              
                self._amprofile.append(pt)
                self._schedule.append(d)
            except StopIteration:
                break
        
    def setschedule(self,xmlvec):
        print "Asset:setschedule"
        for v in xmlvec:
        
            d=xmlvec[v]
            
            if isinstance(d,unicode):
                d1=date(1900,1,1)
                d1=d1.fromordinal(d1.toordinal()+int(d)-2)
                
            else:
                d1=d
            p=MySchedulePt(d1,0.0)
            self._schedule.append(p)
            
    def setCoupn(self,coupon,rates,indx=None):
        if indx!=None:
        
            self._coupon.ctype="Floating"
            self.cpnType="floating"
            self.index=indx
            
            self._coupon.index=indx
            self._coupon.rates=rates
            print coupon.daycountconvention
            self._coupon.daycount.setType(coupon.daycountconvention)
            self.dc.setType(coupon.daycountconvention)
        else:
            self._coupon.ctype="Fixed"
            self.cpnType="fixed"
        print self    
        self._coupon.rates=rates
        self.cpn=rates[0]
        print "cpn rate/spread= ",rates[0]
        pass

    def buildCFs(self):
        if len(self._coupon._rates)==1:
            print "super building cfs"
            super(MyAsset,self).buildCFs()
            
        else:
            print "building child cfs"
        
    @prop
    def atype():pass
    @prop
    def state():pass
    @prop
    def currency():pass
    
    def __str__(self):
        return str(self.name)

    def deepCopy(self,instr):
        super(MyAsset,self).deepcopy(instr)
        self._atype=instr._atype
        self._state=instr.state
        self._currency=instr._currency
        self._coupon=instr._coupon
        
##================================================================
## Class Tranche
## Purpose  : A class for Tranche Flows
## Version  : 1.0
## Used by  : 
## Parent   : Instrument
## Children : 
## Comments:  May be better to rename ABSAsset
##           or to factor out an ABS Asset
##           
##
##================================================================             
        
    
class MyTranche(MyInstrument):
   
    def __init__(self):
        self.cdoName=""
        self.trancheName=""
        self.interestPriority=1
        self.principalPriority=1

        print "In Tranche Init"
        super(MyTranche,self).__init__()
        print self._dc,type(self._dc)

    def payInterest(self,d1,d2,notional,c):
            
        if isinstance(c,unicode):
            c=float(c)
        return self.dc.accrual(d1,d2)*notional*c
    def getPeriodRate(self,i):
        if self.cpnType=="floating":
            indx=icrv[i].value
            c=indx+self.cpn
        else:
            c=self.cpn
    def calcPeriodInterestDue(self,i):
        pass
    def calcInterestDue(self,cpn,amnt,d1,d2):
            
        return self.dc.accrual(d1,d2)*amnt*cpn
    
    def setschedule(self,xmlvec):
       
        for v in xmlvec:
        
            d=xmlvec[v]
            
            if isinstance(d,unicode):
                d1=date(1900,1,1)
                d1=d1.fromordinal(d1.toordinal()+int(d)-2)
                
            else:
                d1=d
            p=MySchedulePt(d1,0.0)
            self._schedule.append(p)

    def setCoupn(self,coupon,rates,indx=None):
        if indx!=None:
            print "Floating Coupon"
            self._coupon.ctype="Floating"
            self.cpnType="floating"
            self.index=indx
            self._coupon.index=indx
            self._coupon.rates=rates
            print coupon.daycountconvention
            self._coupon.daycount.setType(coupon.daycountconvention)
            print self._dc,type(self._dc)
            self._dc.setType(coupon.daycountconvention)
        else:
            print "Fixed Coupon"
            self._coupon.ctype="Fixed"
            self.cpnType="fixed"
         
            self._coupon.rates=rates
            print "cpn rate/spread= ",rates[0]
      
    def buildCFs(self):

        i=1
        self.cfs=list()
        
        isch=iter(self._schedule)
        print len(self._schedule)
       
        d1=isch.next().date
        d1=isch.next().date
       

        while True:
                try:
        
                    c=self._coupon.getPeriodRate(i)
                    d2=isch.next().date
                    
                    
                    
                    prin=0.0
                    ob=self.nominal
                    cb=ob-prin
                    
                    intrst=0.0
                    idue=self.payInterest(d1,d2,ob,c)*ob
                    cf=MyTrancheFlow()
                    i=i+1
                    cf.setFlow(d2,ob,cb,intrst,prin,0.0,0.0,0.0,0.0,idue,0.0)
                    self.cfs.append(cf)
                    d1=d2
                except StopIteration:
                    break
    def updateCFs(self):
        pass
    def __str__(self):
        return self.name+" "+str(len(self.cfs))
##================================================================
## Class DefSchedule
## Purpose  : A class for Tranche Flows
## Version  : 1.0
## Used by  : Asset
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================ 
class MyDefSchedule(object):
    # class to provide standard default schedules
   def __init__(self):
        self.defschedule=list()
        self.freq=4
        self.smoothYr1=False
   def Moodys(self,year):
       self.defschedule=list()
       if year > 5:
           print "Year greater than 5"
       else:
           for i in range(1 , 6*self.freq):
              if i< year*self.freq+1 and i>=(year-1)*self.freq+1:
                 amt=.5
              else:
                 amt=.1
              self.defschedule.append(amt/self.freq)
       return self.defschedule
##================================================================
## Class Holding
## Purpose  : A class to determine amount of a particular asset in a portfolio
##            A portfolio is a collection of holdings of an asset.
## Version  : 1.0
## Used by  : Portfolio
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================ 
class Holding(object):
    #class to attribute an Instrument with a nominal amount in a portfolio
    transaction_types=Enum(['BUY','SELL','REDEEM','EXCHG'])
    def __init__(self,instr,amount,dt):
        self.instrument=instr
        self.nominal=amount
        tt=Holding.transaction_types.BUY
        row=(tt,dt,amount)
        self.transactions=list()
        self.transactions.append(row)
    def changeholding(self,amt):
        self.nominal=amt
    def transaction(self,tt,dt,amount):
        row=(tt,dt,amount)
        self.transactions.append(row)
        if tt==Holding.transaction_types.BUY:
            self.nominal=self.nominal+amount
        elif tt==Holding.transaction_types.SELL or tt==Holding.transaction_types.EXCHG or tt==Holding.transaction_types.REDEEM:
                self.nominal=self.nominal-amount
    def generateCFs(self):
        self.instrument.setNotional(self.nominal)
        self.instrument.updateCFs()
        return self.instrument.cfs
##================================================================
## Class Portfolio
## Purpose  : A collection of holdings
## Version  : 1.0
## Used by  :
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================            
class MyPortfolio:
    #class to provide a collection of Instruments
    def __init__(self):
        self.holdings=list()
        self._determination_dates=list()
        self.cfs=list()
    def init_cfs(self):
        for p in self._determination_dates:
            cf =  MyFlow()
            cf.setPD(p.date)
            self.cfs.append(cf)
    def addHolding(self,h):
        self.holdings.append(h)
    def setDDates(self,dd):
        self._determination_dates=dd
    def getDDates(self):
        return self._determination_dates
    def aggregateCFs(self):
        self.init_cfs()
  
        n=len(self._determination_dates)-1
        id1=self._determination_dates[0].date.toordinal()
        id2=self._determination_dates[n].date.toordinal()
        m=(id2-id1)*1.0/(n*1.0)
        ob=0.0
        for h in self.holdings:
            cfs=h.generateCFs()
            ob+=h.nominal
            for cf in cfs:
                d=cf.pd
                id=d.toordinal()
                i=int((id-id1)/m)+1
                while id >= self.cfs[i].pd.toordinal():
                    i=i+1
                while id < self.cfs[i-1].pd.toordinal():
                    i=i-1
                self.cfs[i].interest+=cf.interest
                self.cfs[i].principal+=cf.principal
                self.cfs[i].default+=cf.default 
                self.cfs[i].assrecovery+=cf.assrecovery
                self.cfs[i].recovery+=cf.recovery
                self.cfs[i].prepay+=cf.prepay
        
        for cf in self.cfs:
            cf.opening_balance=ob
            cb=ob-cf.principal-cf.default-cf.prepay
            cf.closing_balance=cb
            ob=cb
##=================================================================
## Class AccountFlow
## Purpose  : A class for Account Flows
## Version  : 1.0
## Used by  : Account
## Parent   : object
## Children : 
## Comments: Should be factored from Flow
##           
##
##================================================================
class MyAccountFlow(object):
        def __init__(self):
                self.pd=date.today()
                self.opening_balance=0.0
                self.closing_balance=0.0
                self.interest=0.0
                self.debit=0.0
                self.credit=0.0
        def setFlow(self,d,ob,cb,i,p,c,r,ar,pp):
                self.pd=d
                self.opening_balance=ob
                self.debit=p
                self.credit=c
                self.interest=i
                self.closing_balance=ob+self.credit-self.debit
        def __str__(self):
                rep=str(self.pd)
                rep += ", "+ str(self.opening_balance) +", "
                rep += str(self.credit) +", "
                rep += str(self.debit) + ", "
                rep += str(self.interest) + ", "
                rep += str(self.prepay) + ", "
                rep += str(self.closing_balance)
                return rep
        def __repr__(self):
                rep=str(self.pd)
                rep += ", "+ str(self.opening_balance) +", "
                rep += str(self.credit) +", "
                rep += str(self.debit) + ", "
                rep += str(self.interest) + ", "
                rep += str(self.prepay) + ", "
                rep += str(self.closing_balance)
                return rep

        def getPD(self):
                return self.pd
        def getOB(self):
                return self.opening_balance
        def getCB(self):
                return self.closing_balance
        def getI(self):
                return self.interest
        def getCredit(self):
                return self.credit
        def getDebit(self):
                return self.debit
        def setPD(self,payd):
                 self.pd=payd
        def setOB(self,ob):
                self.opening_balance=ob
        def setCB(self,cb):
                self.closing_balance=cb
        def setI(self,i):
                 self.interest=i
        def setCredit(self,p):
                 self.credit=p
        def setDebit(self,d):
                 self.debit=d
        def addCredit(self,p):
                self.credit+=p
        def takeDebit(self,p):
                self.debit-=p
        def getCurrentBalance(self,i):
            return self.opening_balance-self.debit+self.credit

##================================================================
## Class Account
## Purpose  : A class for Accounts
## Version  : 1.0
## Used by  : 
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================    
class MyAccount(object):
    def __init__(self,pd,ob):
        self._name=""
        self._balances=list()
        self._paydates=pd
        self._openingbalance=ob
        
    @prop
    def name():pass
    @prop
    def balances():pass
    @prop
    def paydates():pass
    @prop
    def openingbalance():pass

    def init_balances(self,paydates,ob):
        for pd in paydates:
            af=MyAccountFlow()
            af.setPD(pd.date)
            af.setOB(ob)
            self.balances.append(af)

    def credit(self,pd,amt):
        try:
            i=self.paydates.index(pd)
            self.balances[i].addCredit(amt)
        except ValueError:
           print "Payment Date",pd, "not valid "
           pass
            
    def debit(self,amt,pd):
        try:
            i=self.paydates.index(pd)
            self.balances[i].takeDebit(amt)
        except ValueError:
           print "Payment Date",pd, "not valid "
           pass
    def getOB(self,i):
        return self.balances[i].getOB()
    def getCB(self,i):
        return self.balances[i].getOB()

    def makePayment(self,i,p=None):
        if p> self.getCurrentBalance(i) or p==None:
            p=self.getOB(i)
        self.balances[i].takedebit(p)
        return p
    def pd(self,i):
        return self.paydates[i]
##================================================================
## Class Fee
## Purpose  : A class for Fees
## Version  : 1.0
## Used by  : 
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================    
class MyFee(object):
    _name=""
    _ftype=""
    _index=None
    _dc=None
    _cap=100.00
    _floor=0.00
    _continuous=False
    _rates=None
    _notionals=None
    def __init__(self):
        self._dc=MyDayCount()
        self._rates=list()
        self._notionals=list()
    @prop
    def name(): pass
    @prop
    def ftype(): pass
    @prop
    def index():pass
    @prop
    def dc():pass
    @prop
    def cap():pass
    @prop
    def floor():pass
    @prop
    def continuous():pass
    @prop
    def rates():pass

##================================================================
## Class Curves
## Purpose  : A class for Curves
## Version  : 1.0
## Used by  : 
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================    
class MyCurve(object):
    def __init__(self):
        self._name=""
        self._annualized=False
        self._dc=MyDayCount()
        self._conditional=False
        self._rates=list()
    @prop
    def name(): pass
    @prop
    def annualized():pass
    @prop
    def dc():pass
    @prop
    def conditional():pass
    @prop
    def rates():pass

##================================================================
## Class HedgeLeg
## Purpose  : A class for Hedges
## Version  : 1.0
## Used by  : 
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================
class MyHedgeLeg(object):
    def __init__(self):
        self._ltype=None
        self._assetName=""
        self._notional=0.0
        self._coupon=None
        self._asset=None

    @prop
    def ltype():pass
    @prop
    def assetName():pass
    @prop
    def notional():pass
    @prop
    def coupon():pass
    @prop
    def asset():pass

    def setType(self,ltype):
        self._ltype=ltype
    def addAsset(self,an,asset):
        self.assetName=an
        self.asset=asset
    
##================================================================
## Class Hedges
## Purpose  : A class for Hedges
## Version  : 1.0
## Used by  : 
## Parent   : object
## Children : 
## Comments:
##           
##
##================================================================    
class MyHedge(object):
    def __init__(self):
        self._name=""
        self._htype=None
        self._state=None
        self._legs=list()
    
    @prop
    def name():pass
    @prop
    def htype():pass
    @prop
    def state():pass
    @prop
    def legs():pass

    def addLeg(self,leg):
        self._legs.append(leg)
    
