class Unit:
    def __init__(self,unitid,unitaddress,unitname,unit_propertyid,unitstatus,unitdescription):
        self._unitid = unitid
        self._unitaddress = unitaddress
        self._unitname = unitname
        self._unit_propertyid = unit_propertyid
        self._unitstatus = unitstatus
        self._unitdescription = unitdescription
    # Unit ID
    @property
    def unitid(self):
        return self._unitid
    @unitid.setter
    def unitid(self, value):
        self._unitid = value
    
    # Unit Address
    @property
    def unitaddress(self):
        return self._unitaddress    
    
    @unitaddress.setter
    def unitaddress(self, value):
        self._unitaddress = value   
    
    # Unit Name
    @property
    def unitname(self): 
        return self._unitname
    
    @unitname.setter
    def unitname(self,value):
        self._unitname = value
    
    # Unit Property ID
    @property
    def unit_propertyid(self):
        return self._unit_propertyid
    
    @unit_propertyid.setter
    def unit_propertyid(self, value):
        self._unit_propertyid = value       
    
    # Unit Status
    @property
    def unitstatus(self):
        return self._unitstatus
    
    @unitstatus.setter
    def unitstatus(self, value):
        self._unitstatus = value
    
    # Unit Description
    @property
    def unitdescription(self):
        return self._unitdescription
    
    @unitdescription.setter
    def unitdescription(self, value):
        self._unitdescription = value
        
    def __str__(self):
        return (
            f"Unit ID: {self.unitid}\n"
            f"Unit Name: {self.unitname}\n"
            f"Address: {self.unitaddress}\n"
            f"Property ID: {self.unit_propertyid}\n"
            f"Status: {self.unitstatus}\n"
            f"Description: {self.unitdescription}\n"
        )
