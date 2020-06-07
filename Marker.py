class Marker(object):
    m_owner = 0
    m_location = 0

    def __init__(self,x_id):
        self.m_location = 1

        
    def m_calclocation(self,x_dieroll):
        x_calcvalue = (self.m_location * x_dieroll)
        return x_calcvalue

    def m_setlocation (self,x_newlocation):
        self.m_location = x_newlocation

    def m_get_location(self):
        return self.m_location

    def m_get_status(self):
        if self.m_location == 120: 
            return False
        else:
            return True






