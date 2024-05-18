class Aviacompany:
    plane_list = list()
    rout_list = list()
    def add_plane(self, name):
        self.plane_list.append(name)
        print(self.plane_list)
        return self.plane_list
    def del_plane(self, name):
        self.plane_list.pop(self.plane_list.index(name))
        print(self.plane_list)
        return self.plane_list
    def add_rout(self, name):
        self.rout_list.append(name)
        print(self.rout_list)
        return self.rout_list
    def del_rout(self, name):
        self.rout_list.pop(self.plane_list.index(name))
        print(self.rout_list)
        return self.rout_list
    def find_plane(self, model):
        print(*[plane for plane in self.plane_list if model == plane])
        return [plane for plane in self.plane_list if model == plane]
    def find_rout(self, city):
        print(*[rout for rout in self.rout_list if city in rout])
        return [rout for rout in self.rout_list if city in rout]

aero = Aviacompany()
aero.add_plane('bz')
aero.add_rout('a - b')
aero.add_rout('d - f')
aero.find_rout('d')
