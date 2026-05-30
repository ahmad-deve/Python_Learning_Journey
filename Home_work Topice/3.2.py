class stu:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if len(new_name) < 3:
            print("Name too short!")
        else:
            self._name = new_name
s = stu("Ahmad")
print(s.name)
s.name = "ali"
print(s.name)
s.name = "a"
print(s.name)
