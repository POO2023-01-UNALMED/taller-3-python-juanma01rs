class Control:
   
    def __init__(self):
        self._tv = None
        
    def turnOn(self):
        self.tv.turnOn()
        
    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()
        
    def canalDown(self):
        self.tv.canalDown()
    
    def volumentUp(self):
        self.tv.volumentUp()
        
    def volumentDown(self):
        self.tv.volumentDown()
                   
    def setCanal(self, canal):
        self.tv.setCanal(canal)            
        
    def enlazar (self, tv):
        self._tv = tv
        tv.setControl(self)
    
    def setTv (self, tv):
        self._tv = tv
    
    def getTv (self):
        return self._tv
        