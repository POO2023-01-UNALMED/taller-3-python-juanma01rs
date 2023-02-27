class Control:
   
    def __init__(self, tv):
        self._tv = tv
        
    def turnOn(self):
        self.tv.turnOn()
        
    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()
        
    def canalDown(self):
        self.tv.canalDown()
    
    def volumentUp(self):
        self.tv.volumenUp()
        
    def volumentDown(self):
        self.tv.volumenDown()
                   
    def setCanal(self, canal):
        self.tv.setCanal(canal)            
        
    def enlazar (self, tv):
        self._tv = tv
        tv.setControl(self)
    
    def setTv (self, tv):
        self._tv = tv
    
    def getTv (self):
        return self._tv
        