class Lease:
    def __init__(self, lease_number, property_number, address, start_date, end_date, status=None):
        self._lease_number = lease_number
        self._property_number = property_number
        self._address = address
        self._start_date = start_date
        self._end_date = end_date
        self._status = status

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

    # Address
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

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

    def __str__(self):
        return (f"Lease #{self.lease_number} for Property #{self.property_number}, "
                f"Address: {self.address}, Start: {self.start_date}, End: {self.end_date}, Status: {self.status}")