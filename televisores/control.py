class Control:
    import tv
    tv.turnOn()
    tv.turnOff()
    tv.canalUp()
    tv.canalDown()
    tv.volumenUp()
    tv.volumenDown()
    tv.setCanal()
    
    def __init__(self):
        self._tv = None
        
    def enlazar (self, televisor):
        self._tv = televisor
        self.tv._control = self
    
    def setTv (self, televisor):
        self._tv = televisor
    
    def getTv (self):
        return self._tv
        