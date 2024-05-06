class Nikola:
    def __init__(self, name, age: int):
        if name != 'Николай':
            self.name = f'Я не {name}, а Николай'
        else:
            self.name = name
        self.age = age
        print(self.name)

eblan = Nikola('МАКСДАУН', -4)
