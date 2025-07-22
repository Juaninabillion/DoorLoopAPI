class Lease:
    def __init__(self, lease_number, property_number, start_date, end_date,units, lease_type=None,status=None):
        self._lease_number = lease_number
        self._property_number = property_number
        self._start_date = start_date
        self._end_date = end_date
        self._status = status
        self._units = units or []
        self._lease_type = lease_type

    # Lease Number
    @property
    def lease_number(self):
        return self._lease_number

    @lease_number.setter
    def lease_number(self, value):
        self._lease_number = value

    # Property Number
    @property
    def property_number(self):
        return self._property_number

    @property_number.setter
    def property_number(self, value):
        self._property_number = value

    # Start Date
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    # End Date
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    # Status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def units(self):
        return self._units 
    
    @units.setter
    def units(self,value):
        self._units = value

    @property
    def lease_type(self):
        return self._lease_type

    @lease_type.setter
    def lease_type(self,value):
        self._lease_type = value

  

    def __str__(self):
        return (f"Lease #{self.lease_number} ({self.lease_type}) for Property #{self.property_number}, "
                f"Start: {self.start_date}, End: {self.end_date}, Status: {self.status}, "
                f"Units: {self.units}")