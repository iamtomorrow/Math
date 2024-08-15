from manim import *

class SquareArea(Scene):

    def construct(self):
        # CREATE THE SQUARE
        square = Square(side_length=3, color=ORANGE)
        square.shift(UP*1.5) # SHIFTING SQUARE UPWARD

        # CREATE LABELS FOR THE SIDES OF THE SQUARE
        side_label = MathTex("L").next_to(square, LEFT)
        side_label2 = MathTex("L").next_to(square, DOWN)

        # ANIMATE THE DRAWING OF THE SQUARE AND SIDE LABELS
        self.play(Create(square))
        self.play(Write(side_label), Write(side_label2))

        # DISPLAY THE FORMULA FOR THE AREA OF A SQUARE
        area_formula = MathTex("Area = L^2").shift(DOWN*2)
        self.play(Write(area_formula))

        # SHOW THE CALCULATION FOR A SPECIFIC SIDE LENGTH
        side_value = MathTex("L = 2").shift(DOWN*2.5)
        area_calculation = MathTex("Area = 2^2 = 4").shift(DOWN*3)
        self.play(Write(side_value))
        self.play(Transform(area_formula, area_calculation))

        # HIGHLIGHT THE AREA OF THE SQUARE
        square_area = Square(side_length=3, fill_color=ORANGE, fill_opacity=0.75)
        square_area.shift(UP*1.5)
        self.play(FadeIn(square_area))

        # PAUSE FOR A MOMENT
        self.wait(3)

        # FINISH
        self.play(FadeOut(square), FadeOut(square_area), FadeOut(area_formula), FadeOut(side_label), FadeOut(side_label2))
