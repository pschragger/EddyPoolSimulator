import simbase as esim

class TestEvent(esim.Event):
    def __init__(self, env, name, firsttime):
        self.env = env
        self.name = name
        self.eventtime = firsttime
        self.eventcount = 0

    def Run(self,eventtime):
        """Run the test events"""        
        if self.eventcount == 0:
            print("TestEvent event: %self.name% first submitted")
            newevent = esim.Event(env, "testevent %self.name%",  self , self.firsttime, [] )
            env.EventQue.push(newevent)
        elif self.eventcount < self.maxnumber:
            #Schedule Next Event
            eventtime = env.simclock.time + self.interval
            newevent = esim.Event(self.env, "testevent %self.name%",  self.run, eventtime, [] )
            env.EventQue.push(newevent)
            #process testevent
            print("TestEvent event: %self.name% ran  %env.simclock.time%")


simenv = esim.ENV()

test1 = TestEvent( simenv, "TEST1 OBJECT", 10);

simenv.eventq.push(test1)

simenv.run()
