from manim import *

class TriangleArea(Scene):

    def construct(self):
        # INTRO TITLE
        title = MathTex("Triangle Area")

        # CREATE THE TRIANGLE
        triangle = Polygon(
            [-2, -1, 0], # Point A
            [2, -1, 0], # Point B
            [0, 2, 0], # point C
            color=BLUE
        )
        triangle.shift(UP*1.5)

        # CREATE LABELS FOR THE SIDES OF THE TRIANGLE
        side_label = MathTex("b").next_to(triangle, DOWN)
        side_label2 = MathTex("h").next_to(triangle, LEFT)

        # ANIMATE THE DRAWING OF THE TRIANGLE AND SIDE LABELS
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        self.play(Create(triangle))
        self.play(Write(side_label), Write(side_label2))

        # DISPLAY THE FORMULA FOR THE AREA OF A SQUARE
        area_formula = MathTex("Area = \\frac{1}{2} \\times b \\times h)").shift(DOWN*2)
        self.play(Write(area_formula))

        # SHOW THE CALCULCATION FOR A SPECIFIC BASE AND HEIGHT
        base_value = MathTex("b = 2").shift(DOWN*1.6).shift(LEFT*3)
        height_value = MathTex("h = \sqrt{3}").shift(DOWN*1.6).shift(RIGHT*3)
        area_calculation = MathTex("Area = \\frac{1}{2} \\times 2 \\times \sqrt{3} = \sqrt{3}").shift(DOWN*3)

        self.play(Write(base_value), Write(height_value))
        self.play(Transform(area_formula, area_calculation))

        self.wait(3)

        # HIGHLIGHT THE AREA OF THE TRIANGLE
        triangle_area = Polygon(
            [-2, -1, 0], # Point A
            [2, -1, 0], # Point B
            [0, 2, 0], # point C
            fill_color=BLUE,
            fill_opacity=1
        )
        triangle_area.shift(UP*1.5)
        self.play(FadeIn(triangle_area))

        #PAUSE FOR A MOMENT
        self.wait(3)

        # FINISH
        self.play(
            FadeOut(triangle),
            FadeOut(side_label),
            FadeOut(side_label2),
            FadeOut(area_formula),
            FadeOut(base_value),
            FadeOut(height_value),
            FadeOut(area_calculation),
            FadeOut(triangle_area)
        )
