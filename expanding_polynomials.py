from manim import *

class Polynomial(Scene):
    
    def construct(self):
        # INTRO TITLE
        title = MathTex("Expanding Polynomials")

        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # CREATE THE POLYNOMIAL
        polynomial1 = MathTex("a^2 + 2ab + b^").shift(UP)
        polynomial2 = MathTex("(a + b) \\times (a + b)").shift(DOWN)
        self.play(Transform(polynomial1, polynomial2))
        self.wait(3)

        polynomial3 = MathTex("(a + b)^2")
        self.play(Write(polynomial3))

        self.wait(1)

        self.play(FadeOut(polynomial1), FadeOut(polynomial2), FadeOut(polynomial3))
