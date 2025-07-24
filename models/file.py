class File:
    def __init__(self, file_id,file_resource_id,file_name,file_unit_id,file_property_id):
        self._file_id = file_id
        self._file_resource_id = file_resource_id
        self._file_name = file_name
        self._file_unit_id = file_unit_id
        self._file_property_id = file_property_id
    # File ID
    @property
    def file_id(self):
        return self._file_id    
    @file_id.setter 
    def file_id(self, value):
        self._file_id = value
    # File Type
    @property
    def file_resource_id(self):
        return self._file_resource_id
    @file_resource_id.setter
    def file_resource_id(self, value):
        self._file_resource_id = value
    # File Name
    @property
    def file_name(self):
        return self._file_name
    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    # File Unit ID
    @property
    def file_unit_id(self):
        return self._file_unit_id       
    @file_unit_id.setter
    def file_unit_id(self, value):
        self._file_unit_id = value
    # File Property ID
    @property
    def file_property_id(self):
        return self._file_property_id
    @file_property_id.setter
    def file_property_id(self,value):
        self._file_property_id = value
    
    def __str__(self):
        return f"File ID: {self.file_id}\n" \
                f"File Type: {self.file_resource_id}\n" \
               f"File Name: {self.file_name}\n" \
               f"File Unit ID: {self.file_unit_id}\n" \
               f"File Property ID: {self.file_property_id}\n"
    