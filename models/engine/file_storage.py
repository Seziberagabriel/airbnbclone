import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects currently stored in FileStorage.
        
        The keys are in the format <class name>.<object id> and the values are 
        the corresponding object instances.
        """

        return self.__objects
    
    def new(self, new_obj):
        """
        Adds a new object to the FileStorage's dictionary of objects.
        
        The new object is stored in the dictionary with a key in the format
        <class name>.<object id>. The object is then saved to disk (see
        save()).
        
        Parameters
        ----------
        new_obj : BaseModel
            The new object to be added to the dictionary of objects.
        """
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.__objects[key] = new_obj

    def save(self):
        objects = {}
        for key, obj in self.__objects.items():
            objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(objects, f)
    
    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:
                dict_objects = json.load(f)
                for key, obj in dict_objects.items():
                    self.__objects[key] = BaseModel(**obj)
        except FileNotFoundError:
            pass