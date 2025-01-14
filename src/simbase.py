import bisect

INFINITY = 999999999999999

class Clock:
    def __init__(self, env, smallestinterval):
        self.env = env
        self.smallestinterval = smallestinterval
        self.currenttime = 0

    def GetTime(self):
        """return the clock's current time"""        
        return self.currenttime

    def AdvanceTime(self, interval):
        """advance the clock by the external interval"""        
        self.currenttime = self.currenttime + interval

class Event:
    def __init__(self, env, name, process, eventtime  ):
        self.env = env
        self.name = name
        self.process = process
        self.eventtime = eventtime
        self.paramlist = paramlist
        
    def Process(self):
        """run the event's process """        
        self.process.run(self.eventtime, self.paramlist )

    def GetEventTime(self):
        """Return the start time of the event """        
        return self.eventtime

    def Run(self):
        """Placeholder event """
        print("%self.eventtime% - %self.name% Event running")

class NULLEvent(Event):
    def __init__(self):
        self.eventtime = INFINITY
        self.name = "NULLEVENT"
        
class EventQueue:
    def __init__(self, env ):
        self.env = env
        self.eventq = []

    def  push(self, event ):
        inserttime = event.GetEventTime()
        new_tuple = ( inserttime, event)
        if len(self.eventq) == 0:
            self.eventq = [ new_tuple ]
        else:
            index = bisect.bisect(self.eventq, new_tuple)          
            # Use bisect to find the correct insertion point
            # Insert the new tuple while maintaining the sorted order
            self.eventq.insert(index, new_tuple)

    def pop(self):
        topevent = self.eventq[0]
        self.eventq.remove(topevent)
        return topevent
    
class ENV:
    def __init__(self):
        self.clock = Clock(self, 1 )
        self.eventq = EventQueue(self)
        self.NULLEVENT = NULLEvent()
        self.eventq.push(self.NULLEVENT)

    def run(self):
        nextevent = self.eventq.pop()
        while ( nextevent != self.NULLEVENT ):
            time, currentevent = nextevent
            currentevent.Run(self.clock.GetTime())
            currentevent = self.eventq.pop()
            

