# A to Z reminding

# Ch10 practice Getter/Setter

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name


    def get_name(self):
        print('inside the getter')
        return self.hidden_name


    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())
# don.hidden_name = 'Go'
# print(don.get_name())
