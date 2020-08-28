items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}


class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start = start_time
    self.end = end_time
  def __repr__(self):
    return self.name + ' menu is available from ' + str(self.start) + ' to ' + str(self.end)
  def calculate_bill(self, purchased_items):
    self.bill = 0
    for i in purchased_items:
      self.bill += self.items[i]
    return self.bill

brunch = Menu('Brunch', items, 11, 16)
#print(brunch)
#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
early = Menu('Earlybird', early_bird, 15, 18)
#print(early.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
evening = Menu('Dinner', dinner, 17, 23)
children = Menu('Kids', kids, 11, 21)


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    menu = []
    for i in self.menus:
      if time>=i.start and time<=i.end:
        menu.append(i)
    return menu


flagship_store = Franchise('1232 West End Road',[brunch,early,evening,children])

new_installment = Franchise('12 East Mulberry Street',[brunch,early,evening,children])

print(flagship_store.available_menus(17))


arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas = Menu('Arepas', arepas_menu, 10, 20)

arepas_place = Franchise('189 Fitzgerald Avenue',[brunch,early,evening,children,arepas])



class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

business = Business("Basta Fazoolin' with my Heart",[flagship_store, new_installment])

new_business = Business("Take a' Arepa",[flagship_store, new_installment, arepas_place])

print(new_business.franchises[2].menus[4])

