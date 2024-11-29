import simbase as esim

class TestEvents:
    def __init(self, env, name, firsttime, interval, maxnumber):
        self.env = env
        self.name = name
        self.firttime = firsttime
        self.interval = interval
        self.maxnumber = maxnumber
        self.eventcount = 0

    def run(self,eventtime, paramlist):
        
        if self.eventcount == 0:
            print("TestEvent event: %self.name% first submitted")
            newevent = esim.Event(env, "testevent %self.name%",  self , self.firsttime, [] )
            env.EventQue.push(newevent)
        elif self.eventcount < self.maxnumber:
            #Schedule Next Event
            eventtime = env.simclock.time + self.interval
            newevent = esim.Event(env, "testevent %self.name%",  self.run, eventtime, [] )
            env.EventQue.push(newevent)
            #process testevent
            print("TestEvent event: %self.name% ran  %env.simclock.time%")


simenv = esim.env()

test1 = TestEvent( simenv, "TEST1 OBJECT", 10, 10, 10);
test1.run()

simenv.run()
