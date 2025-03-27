from manim import *

class Exponents(Scene):
    def construct(self):

        # Title
        title = Tex("Expoentes")
        title.scale(1.5)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        # Exponents
        exp = MathTex(r"2^3 = 2 \times 2 \times 2 = 8")
        exp.scale(1.5)
        self.play(Write(exp))
        self.wait(3)
        self.play(FadeOut(exp))

        # Exponents with base 10
        exp_base_10 = MathTex(r"10^3 = 10 \times 10 \times 10 = 1000")
        exp_base_10.scale(1.5)
        self.play(Write(exp_base_10))
        self.wait(3)
        self.play(FadeOut(exp_base_10))

        # Exponents with base 10 and negative exponent
        exp_base_10_neg = MathTex(r"10^{-3} = \frac{1}{10^3} = \frac{1}{10 \times 10 \times 10} = \frac{1}{1000}")
        exp_base_10_neg.scale(1.5)
        self.play(Write(exp_base_10_neg))
        self.wait(3)
        self.play(FadeOut(exp_base_10_neg))

        # Exponents with base 10 and fractional exponent
        exp_base_10_frac = MathTex(r"10^{0.5} = \sqrt{10} \approx 3.16")
        exp_base_10_frac.scale(1.5)
        self.play(Write(exp_base_10_frac))
        self.wait(3)
        self.play(FadeOut(exp_base_10_frac))

        # Exponents with base 10 and fractional exponent
        exp_base_10_frac = MathTex(r"4^{\frac{1}{2}} = \sqrt{4} =2")
        exp_base_10_frac.scale(1.5)
        self.play(Write(exp_base_10_frac))
        self.wait(3)
        self.play(FadeOut(exp_base_10_frac))

        # Exponents with base 10 and fractional exponent