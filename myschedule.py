import datetime
from datetime import timedelta
from datetime import date
from cdoconfig import prop
from collections import MutableSequence

class MySchedulePt(object):
    def __init__(self,d1,val):
        self._date=d1
        self._value=val

    @prop
    def date():pass

    @prop
    def value():pass
    
##    def setDate(self,d):
##        self.date=d
##    def setValue(self,v):
##        self.value=v
##    def getDate(self):
##        return self.date
##    def getValue(self):
##        return self.value
    def __repr__(self):
        return "("+str(self.date) + ", "+ str(self.value)+")"
    def __str__(self):
        return  str(self.date) + ", "+ str(self.value)

class MySchedule(MutableSequence):
    def __init__(self):
        _schedule=list()

    def __setitem__(self,b,c):
        _schedule[b]=c
    def __getitem__(_schedule,b):
      return _schedule[b]
    def __contains__(self,b):
        return _schedule.__contains__(b)
    def __iter__(self):
        return _schedule.__iter__()
    def __reversed__(self):
        return _schedule.__reversed__(self)
    def insert(self,i,a):
        _schedule.insert(i,a)
   

class MyScheduleGenerator(object):
    

    def __init__(self):
         self._schedule=list()
         self._sd=date.today()
         self._md=date.today()
         self._tenor=5
         self._tenor_type="year"
         self._adj=timedelta(days=1)
         self._frq=1
         self._payday=15
         self._doAdjust=True
        
        
    @prop
    def sd():pass
    @prop
    def schedule():pass
    @prop
    def md():pass
    @prop
    def tenor():pass
    @prop
    def tenor_type():pass
    @prop
    def adj():pass
    @prop
    def frq():pass
    @prop
    def payday():pass
    @prop
    def doAdjust():pass
    
##    def setSD(self,d):
##        self.sd=d
##    def getSD(self):
##        return self.sd
##    def getMD(self):
##        return self.md
##    def setMD(self,d):
##        self.md=d
##    def setTenor(self,t):
##        self.tenor=t
##    def getTenor(self):
##        return self.tenor
##    def getTT(self):
##        return tenor_type
##    def setTT(self,tt):
##        self.tenor_type=tt
##    def getAdjust(self):
##        return self.adj
##    def setAdjust(self,ad):
##        self.adj=ad
##    def setDoAdjust(self,torf):
##        self.DoAdjust=torf
##    def getDoAjust(self):
##        return DoAdjust
##    def getfrq(self):
##        return self.frq
##    def setfrq(self,f):
##        self.frq=f
    def adjust(self,dt):
      while dt.weekday() >4:
          dt=dt+self.adj
      return dt
    def getpayDay(self):
      return payday
    def setpayDay(self,dt):
        self.payday=dt
    def getSchedule(self):
        return self.schedule
        
    def addTime(self,dt,amt,tt):
        if tt=="d":
           dt=dt+amt*self.adj
        elif tt=="w":
           dt=dt+amt*self.adj*7
        elif tt=="y":
            y=dt.year
            y=y+amt
            dt=dt.replace(year=y,day=self.payday)
        elif tt=="m":
           m=dt.month
           y=dt.year
           y=y+int(amt/12)
           amt=amt-int(amt/12)*12
           m=m+amt
         
           if m > 12:
               y=y+1
               m=m-12
           try:
                dt=dt.replace(year=y,month=m,day=self.payday)
           except ValueError:
                print "year=",y," ,month=",m," ,day=",self.payday," ,amt=",amt
        else:
            print "Unknown time type, none of d,w,y,m"
        return dt
    def generate(self):
        d=self.sd
        pt=MySchedulePt(d,0.0)
        self.schedule.append(pt)
        while d<self.md:
            d=self.addTime(d,12/self.frq,"m")
            if self.doAdjust==True:
                d=self.adjust(d)
            pt=MySchedulePt(d,0.0)
            self.schedule.append(pt)
        return self.schedule
    
    def __str__(self):
        rep=list()
        for pt in self.schedule:
            rep.append(pt.__str__())
        return rep

##    def makeschedule(dates,values)
##        schedule=list()
##         for d,v in dates,values:
##             p=MySchedulePt(d,v)
##             schedule.append(p)
##        return schedule







    
