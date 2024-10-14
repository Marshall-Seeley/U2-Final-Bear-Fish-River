# Marshall Seeley
# U2 Final
# Bear Fish River




# Imports:
import random


class River():
  def __init__(self, size, num_bears, num_fish):

    # Attributes:
    self.river = [[0 for x in range(size)] for y in range(size)]
    self.opentiles = [[0 for x in range(size)] for y in range(size)]
    self.size = size
    self.num_bears = num_bears
    self.num_fish = num_fish
    self.animals = []
    self.babies = []
    self.population = 0


    # Actions:
    def __initial_population():
      for i in range(self.num_bears):
        x_coordinate = random.randint(0, self.size - 1)
        y_coordinate = random.randint(0, self.size - 1)
        while self.river[y_coordinate][x_coordinate] != 0:
          x_coordinate = random.randint(0, self.size - 1)
          y_coordinate = random.randint(0, self.size - 1)
        Bear = Bear(x_coordinate, y_coordinate)
        self.animals.append(Bear)
        self.population += 1
      for i in range(self.num_fish):
        x_coordinate = random.randint(0, self.size - 1)
        y_coordinate = random.randint(0, self.size - 1)
        while self.river[y_coordinate][x_coordinate] != 0:
          x_coordinate = random.randint(0, self.size - 1)
          y_coordinate = random.randint(0, self.size - 1)
        Fish = Fish(x_coordinate, y_coordinate)
        self.animals.append(Fish)
        self.population += 1

    def place_baby():
      for baby in self.babies:
        if baby == "fish":
          x_coordinate = random.randint(0, self.size - 1)
          y_coordinate = random.randint(0, self.size - 1)
          while self.river[y_coordinate][x_coordinate] != 0:
            x_coordinate = random.randint(0, self.size - 1)
            y_coordinate = random.randint(0, self.size - 1)
          Fish = Fish(x_coordinate, y_coordinate)
          self.animals.append(Fish)
          self.population += 1
        elif baby == "bear":
          x_coordinate = random.randint(0, self.size - 1)
          y_coordinate = random.randint(0, self.size - 1)
          while self.river[y_coordinate][x_coordinate] != 0:
            x_coordinate = random.randint(0, self.size - 1)
            y_coordinate = random.randint(0, self.size - 1)
          Bear = Bear(x_coordinate, y_coordinate)
          self.animals.append(Bear)
          self.population += 1

    def animal_death(animal):
      self.animals.remove(animal)
      self.population -= 1

    def redraw_cells():
      for animal in self.animals:
        self.river[animal.y][animal.x] = animal

    def new_day():
      for animal in self.animals:
        animal.move()
      self.babies = []
      self.place_baby()


    # Magic 'Dunder' Methods:
    def __getitem__():
      return self.river[x][y]

    def __str__():
      # Visualizing the River:
      for y in range(self.size):
        for x in range(self.size):
          if self.river[y][x] == 0:
            print("🟦", end="")
          else:
            print(self.river[y][x], end="")
        print("\n", end="")
      return River





class Animal():
  def __init__(self, x_coordinate, y_coordinate):

    # Attributes:
    self.x = x_coordinate
    self.y = y_coordinate
    self.bred_today = False


    # Actions:
    def death():
      River.animal_death(self)

    def move():
      move = random.randint(1, 4)
      if move == 1:
        if self.x == self.size - 1:
          pass
        else:
          self.x += 1
          River.redraw_cells()
          self.collision(River.river[self.y][self.x])
      if move == 2:
        if self.x == 0:
          pass
        else:
          self.x -= 1
          River.redraw_cells()
          self.collision(River.river[self.y][self.x])
      if move == 3:
        if self.y == self.size - 1:
          pass
        else:
          self.y += 1
          River.redraw_cells()
          self.collision(River.river[self.y][self.x])
      if move == 4:
        if self.y == 0:
          pass
        else:
          self.y -= 1
          River.redraw_cells()
          self.collision(River.river[self.y][self.x])

    def collision(self, animal_2):
      if type(self) == type(animal_2):
        if type(self) == Fish:
          River.babies.append("fish")
        else:
          River.babies.append("bear")
      else:
        if type(self) == Bear:
          self.consume(animal_2)
        else:
          animal_2.consume(self)





class Fish(Animal):
  def __init__(self, x_coordinate, y_coordinate):
    super().__init__(x_coordinate, y_coordinate)


    # Magic 'Dunder' Methods:
    def __str__():
      return('🐟')





class Bear(Animal):
  def __init__(self, x_coordinate, y_coordinate):
    super().__init__(x_coordinate, y_coordinate)

    # Attributes:
    self.max_lives = 10
    self.lives = self.max_lives
    self.eaten_today = False


    # Actions:
    def starve():
      if self.eaten_today == False:
        self.lives -= 1
        if self.lives == 0:
          self.death()

    def consume(self, Fish):
      self.lives += 1
      Fish.death()
      self.eaten_today = True


    # Magic 'Dunder' Methods:
    def __str__():
      return('🐻')
