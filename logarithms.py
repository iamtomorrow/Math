from manim import *

class ExponentialToLogarithm(Scene):
    def construct(self):
        # Definição das equações
        exp_eq = MathTex(r"a^b = c").scale(2)
        log_eq = MathTex(r"\log_a c = b").scale(2)

        # Posicionando a equação inicial no centro
        self.play(Write(exp_eq))
        self.wait(3)

        # Transformando para a equação logarítmica
        self.play(Transform(exp_eq, log_eq))
        self.wait(3)
