"""
This simple animation example shows how to move an item with the keyboard.
"""

import arcade

# Set up the constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 50

MOVEMENT_SPEED = 5

class Person:
    """ Class to represent an Ellipse on the screen """
    def __init__(self, face_x, face_y, left_leg, right_leg, torso_low, torso_high, foot):
        """ Initialize our Person variables """

        # Position
        self.face_x = face_x
        self.face_y = face_y
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.torso_low = torso_low
        self.torso_high = torso_high
        self.foot = foot

        # Vector
        self.delta_x = 0
        self.delta_y = 0

        # Lock to make sure we don't allow continuous jumps
        self.jumping = False
        self.jump_steps = 0
        self.jumping_direction = 1

    def draw(self):
        """ Draw our person """
        arcade.draw_circle_outline(self.face_x , self.face_y + 70, 15, arcade.color.WHITE, 3)
        arcade.draw_line(self.face_x, self.torso_low, self.face_x, self.torso_high, arcade.color.BLACK, 2)
        arcade.draw_line(self.face_x, self.torso_low, self.left_leg, self.foot, arcade.color.BLACK, 2)
        arcade.draw_line(self.face_x, self.torso_low, self.right_leg, self.foot, arcade.color.BLACK, 2)


    def move(self):
        """ Move our person """

        # See if we've gone beyond the border. If so, don't move until moved in opposite direction
        if self.left_leg < 0 and self.delta_x < 0:
            return
        if self.right_leg >= SCREEN_WIDTH and self.delta_x > 0:
            return

        # Move left/right
        self.face_x += self.delta_x
        self.left_leg += self.delta_x
        self.right_leg += self.delta_x


    def jump(self):
        if   self.delta_y == 0:
            return
        if self.jump_steps == 10:
            self.jumping_direction = -1
            # return

        self.jumping = True
        self.face_y += self.delta_y * self.jumping_direction
        self.torso_high += self.delta_y * self.jumping_direction
        self.torso_low += self.delta_y * self.jumping_direction
        self.foot += self.delta_y * self.jumping_direction
        self.jump_steps += (1 * self.jumping_direction)

        if self.jump_steps == 0:
            self.jumping = False
            self.jumping_direction = 1
            self.delta_y = 0

class Ellipse:
    """ Class to represent an Ellipse on the screen """
    def __init__(self, x, y, width, height, color):
        """ Initialize our Ellipse variables """

        # Position
        self.x = x
        self.y = y

        # Size
        self.height = height
        self.width = width

        # Color
        self.color = color

    def draw(self):
        """ Draw our Ellipse """
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height, self.color)


class Flag:
    """ Class to represent a Flag on the screen """
    def __init__(self, x, y):
        """ Initialize our Flag variables """

        # Position
        self.x = x
        self.y = y

    def draw(self):
        """ Draw our flag """
        arcade.draw_line(self.x, 0, self.x, 400, arcade.color.BLACK, 3)
        arcade.draw_rectangle_filled(self.x-30, self.y+260, 65, 45, arcade.color.RED)

class Triangle:
    """ Class to represent a Triangle on the screen """
    def __init__(self, x, y, color):
        """ Initialize our Triangle variables """

        # Position
        self.x = x
        self.y = y

        # Color
        self.color = color

    def draw(self):
        """ Draw our triangle """
        arcade.draw_triangle_filled(self.x + 30, self.y,
                                self.x, self.y - 60,
                                self.x + 60, self.y - 60,
                                self.color)

class Rectangle:
    """ Class to represent a rectangle on the screen """

    def __init__(self, x, y, width, height, angle, color):
        """ Initialize our rectangle variables """

        # Position
        self.x = x
        self.y = y

        # Vector
        self.delta_x = 0

        # Size and rotation
        self.width = width
        self.height = height
        self.angle = angle

        # Color
        self.color = color

    def draw(self):
        """ Draw our rectangle """
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color, self.angle)

    def move(self):
        """ Move our rectangle """

        # Move left/right
        self.x += self.delta_x

        # See if we've gone beyond the border. If so, reset our position
        # back to the border.
        if self.x < self.width / 2:
            self.x = self.width / 2
        if self.x > SCREEN_WIDTH - (self.width / 2):
            self.x = SCREEN_WIDTH - (self.width / 2)


class MyApplication(arcade.Window):
    """
    Main application class.
    """
    def __init__(self, width, height):
        super().__init__(width, height, title="Keyboard control")
        self.rectangle1 = None
        self.rectangle2 = None
        self.triangle1  = None
        self.triangle2  = None
        self.triangle3  = None
        self.triangle4  = None
        self.triangle5  = None

        self.flag = None

        self.ellipse1 = None
        self.ellipse2 = None

        self.person = None

        self.left_down = False



    def setup(self):
        """ Set up the game and initialize the variables. """
        width = RECT_WIDTH
        height = RECT_HEIGHT
        x = SCREEN_WIDTH // 2
        y = SCREEN_HEIGHT // 2
        angle = 0
        color = arcade.color.WHITE

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.rectangle1 = Rectangle(0, 0, 1200, 200, angle, arcade.color.GREEN)
        self.rectangle2 = Rectangle(150, 200, 100, 40, angle, arcade.color.ORANGE)
        self.rectangle3 = Rectangle(300, 275, 100, 40, angle, arcade.color.ORANGE)
        self.triangle1 = Triangle(90, 160, arcade.color.DARK_BLUE_GRAY)
        self.triangle2 = Triangle(150, 160, arcade.color.DARK_BLUE_GRAY)
        self.triangle3 = Triangle(210, 160, arcade.color.DARK_BLUE_GRAY)
        self.triangle4 = Triangle(270, 160, arcade.color.DARK_BLUE_GRAY)
        self.triangle5 = Triangle(330, 160, arcade.color.DARK_BLUE_GRAY)

        self.flag = Flag(550, 160)

        self.ellipse1 = Ellipse(100, 520, 50, 15, arcade.color.WHITE)
        self.ellipse2 = Ellipse(300, 520, 50, 15, arcade.color.WHITE)

        self.person = Person(40, 95, 5, 75, 100, 150, 60)

        self.left_down = False

    def update(self, dt):
        """ Move everything """
        self.rectangle2.move()
        self.person.move()
        self.person.jump()


    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        self.flag.draw()

        self.rectangle1.draw()
        self.rectangle2.draw()
        self.rectangle3.draw()

        self.triangle1.draw()
        self.triangle2.draw()
        self.triangle3.draw()
        self.triangle4.draw()
        self.triangle5.draw()

        self.ellipse1.draw()
        self.ellipse2.draw()

        self.person.draw()

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.LEFT:
            self.person.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.person.delta_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            self.person.delta_y = MOVEMENT_SPEED
            self.checkIfCollidedWithRectangle(True)
        elif key == arcade.key.A:
            self.rectangle2.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.rectangle2.delta_x = MOVEMENT_SPEED
        self.checkIfCollidedWithRectangle(False);
        self.checkIfFlagTouched();
        self.checkIfCollidedWithTriangle();
            # self.person.jump()

    def checkIfCollidedWithRectangle(self,isJump):
        if(isJump):
            if(self.person.face_x+15 >= self.rectangle2.x-50 and self.person.face_x+15 <= self.rectangle2.x-50+self.rectangle2.width):
                if(self.person.face_y+64+MOVEMENT_SPEED > (self.rectangle2.y-self.rectangle2.height)):
                    print("collided at rectangle 2");
                 #   self.setup();
            if(self.person.face_x+15 >= self.rectangle3.x-50 and self.person.face_x+15 <= self.rectangle3.x-50+self.rectangle3.width):
                if(self.person.face_y+64+MOVEMENT_SPEED > (self.rectangle3.y-self.rectangle3.height)):
                    print("collided at rectangle 2");
                   # self.setup();
        else:
            if(self.person.face_x+15 >= self.rectangle2.x-50 and self.person.face_x+15 <= self.rectangle2.x-50+self.rectangle2.width):
                if(self.person.face_y+64 > (self.rectangle2.y-self.rectangle2.height)):
                    print("collided at rectangle 2");
                  #  self.setup();
            if(self.person.face_x+15 >= self.rectangle3.x-50 and self.person.face_x+15 <= self.rectangle3.x-50+self.rectangle3.width):
                if(self.person.face_y+64 > (self.rectangle3.y-self.rectangle3.height)):
                    print("collided at rectangle 2");
                 #   self.setup();
    def checkIfCollidedWithTriangle(self):
        if(self.person.right_leg > self.triangle1.x and
           self.person.right_leg < self.triangle3.x+60 ):
            self.setup();
    def checkIfFlagTouched(self):
        if(self.person.face_x+15 >= self.flag.x ):
            self.setup();
    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.person.delta_x = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.rectangle2.delta_x = 0



def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

main()
