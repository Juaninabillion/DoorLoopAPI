class Property:
    def __init__(self, propertyid, propertyclass, propertytype, propertyname):
        self._propertyid = propertyid
        self._propertyclass = propertyclass
        self._propertytype = propertytype
        self._propertyname = propertyname

    # Property ID
    @property
    def propertyid(self):
        return self._propertyid

    @propertyid.setter
    def propertyid(self, value):
        self._propertyid = value

    # Property Class
    @property
    def propertyclass(self):
        return self._propertyclass

    @propertyclass.setter
    def propertyclass(self, value):
        self._propertyclass = value

    # Property Type
    @property
    def propertytype(self):
        return self._propertytype

    @propertytype.setter
    def propertytype(self, value):
        self._propertytype = value

    # Property Name
    @property
    def propertyname(self):
        return self._propertyname

    @propertyname.setter
    def propertyname(self, value):
        self._propertyname = value

    def __str__(self):
        return (f"Property ID: {self.propertyid}, "
                f"Class: {self.propertyclass}, "
                f"Type: {self.propertytype}, "
                f"Name: {self.propertyname}")
