from manim import *

class NotacaoSigma(Scene):
    def construct(self):
        # Título
        titulo = Tex(r"Desmistificando a Notação Sigma: $\sum$")
        titulo.to_edge(UP)
        self.play(Write(titulo))
        
        # Definição da notação sigma
        sigma_def = MathTex(r"\sum_{i=1}^{n} a_i")
        sigma_def.scale(1.5)
        self.play(Write(sigma_def))
        self.wait(2)

        # Exemplo prático
        exemplo = MathTex(r"\sum_{i=1}^{5} i = 1 + 2 + 3 + 4 + 5 = 15")
        exemplo.next_to(sigma_def, DOWN, buff=1)
        self.play(Transform(sigma_def, exemplo))
        self.wait(2)

        # Expansão da soma com função
        funcao_soma = MathTex(r"\sum_{i=1}^{4} (2i + 1) = (2(1) + 1) + (2(2) + 1) + (2(3) + 1) + (2(4) + 1)")
        funcao_soma.scale(0.9)
        funcao_soma.next_to(exemplo, DOWN, buff=1)
        self.play(Write(funcao_soma))
        self.wait(3)

        # Finalizando
        self.play(FadeOut(titulo, sigma_def, funcao_soma))
