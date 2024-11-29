
class Clock:
    def __init(self, env, smallestinterval):
        self.env = env
        self.smallestinterval = smallestinterval
        self.currenttime = 0

    def GetCurrentSimTime(self):
        return self.currenttime;

    def AdvanceTime(self, interval):
        self.currenttime = self.currenttime + interval

class Event:
     def __init(self, env, name, process, eventtime, paramlist  ):
        self.env = env
        self.name = name
        self.process = process
        self.eventtime = eventtime
        self.paramlist = paramlist

    def Process(self):
        self.process.run(self.eventtime, self.paramlist );

    def GetEventTime(self):
        return self.eventtime
    
        
class EventQueue:
    def __init(self, env ):
        self.env = env
        self.eventq = []

    def  push(self, event ):
        inserttime = event.GetEventTime()
        new_tuple = ( inserttime, event)
        if length.eventq == 0:
            eventq = [ new_tuple ]
        else:
            index = bisect.bisect(eventq, new_tuple)          
            # Use bisect to find the correct insertion point
            # Insert the new tuple while maintaining the sorted order
            eventq.insert(index, new_tuple)

    def pop(self):
        topevent = eventq[0].event
        eventq.remove(topevent)
        return topevent
    
class ENV:
     def __init(self):
         self.clock = clock(self, 1 )
         self.eventq = EventQueue(self)

    def run(self):
        nextevent = self.eventq.pop()
        while ( nextevent != null ):
            nextevent.run()
            nextevent = self.eventq.pop()
            
