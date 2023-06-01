class AirCastle
    def __init__(self, height, num_clouds, color):
        self.height = height
        self.num_clouds = num_clouds
        self.color = color

    def change_height(self, value):
        if self.height - value >= 0:
                self.height -= value

        else:
         self.height = 0
    def add_clouds(self,n):
        self.num_clouds +=n
        self.height +=n//5

    def __call__(self,transparency):
        return self.height // transparency * self.num_clouds

    def __str__(self):
        return f"The AirCastle at an altitude of {self.height} is with {self.num_clouds}."

    def __str__(self, other):
        if self.num_clouds < other.num_clouds:
                return True

        elif self.num_clouds == other.num_clouds
