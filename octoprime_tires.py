from tires import Tires

class OctoprimeTires(Tires):
    
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        int service = 0
        for i in range(4):
            service += self.wear[i]
        if service >= 3:
            return True
        return False

