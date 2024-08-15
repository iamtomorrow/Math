from manim import *

class Pith(Scene):

    def Construct(self):
        
        sq = Square(side_length=5, stroke_color=RED, fill_color=BLACK)

        self.play(Create(sq), run_time=5)
        self.wait(5)

        self.play(sq.animate.set_fill(RED))
        self.wait(5)
        self.play(sq.animate.scale(0.5), run_time=5)
        self.wait(3)
        self.play(FadeOut(sq))
        self.wait(3)
        
pith = Pith()
pith.Construct( )
