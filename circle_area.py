from manim import *

class CircleArea(Scene):

    def construct(self):   
        # CREATE THE CIRCLE
        circle = Circle(radius=1, color=BLUE)
        circle.shift(UP*2)

        # CREATE LABELS FOR THE METRICS OF THE CIRCLE
        radius_label = MathTex("R").next_to(circle, LEFT)

        # ANIMATE THE DRAWING OF THE SQUARE AND METRIC LABELS
        self.play(Create(circle))
        self.play(Write(radius_label))

        # DISPLAY THE FORMULA FOR THE AREA OF THE CIRCLE
        area_formula = MathTex("Area = \pi \\times R^2").shift(DOWN*2)
        self.play(Write(area_formula))

        # SHOW THE CALCULATION FOR A SPECIFIC METRIC

        self.wait(3)

        # HIGHLIGHT THE AREA OF THE CIRCLE
        circle_area = Circle(radius=1, fill_color=BLUE, fill_opacity=1)
        circle_area.shift(UP*2)
        self.play(FadeIn(circle_area))

        # PAUSE FOR A MOMENT
        self.wait(3)

        # FINISH
        self.play(
            FadeOut(circle),
            FadeOut(circle_area),
            FadeOut(area_formula),
            FadeOut(radius_label)
        )
