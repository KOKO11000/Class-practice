class Agent:
    total = 0
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self._clearance_level = clearance_level
    

    def add_agent(self):
        self.total += 1
        print(self.total)

    def sub_agent(self):
        self.total -= 1
        print(self.total)

    def get_clearence_level(self):
        return self._clearance_level
    
    def set_clearence_level(self):
        if clearance_level > 0 or clearance_level < 10:
            self._clearance_level = clearance_level
        else:
            print("clearance must be between 0 - 10! ")


    def report(self):
        print(f"Agent {self.code_name}. Clearance level: {self._clearance_level}")



class mission:
    def __init__(self, mission_name: str, target_location: str,assigned_agent: Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent

    def brief(self):
        print(f"Mission: {self.mission_name}\n Target: {self.target_location}, Agent: {self.assigned_agent.code_name}")



class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level,region):
        super().__init__(code_name, clearance_level)
        self.region = region

    def report(self):
        print(f"Agent {self.code_name}. Clearance level: {self._clearance_level}, is region: {self.region}")

class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level,specialty):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty

    def report(self):
        print(f"Agent {self.code_name}. Clearance level: {self._clearance_level}, is specialty: {self.specialty}")


if __name__ == "__main__":

    clearance_level = Agent("Aharon", 5)
    a1 =CyberAgent('david',2,"snipe")
    a2 =CyberAgent("007",3,"assaian")
    a3 =FieldAgent("07",3,"Yaman")
    a4 =FieldAgent("7",3,"Iran")
    list_of_agent = [a1,a2,a3,a4]
    for i in list_of_agent:
        print(i.add_agent())
        i.report()