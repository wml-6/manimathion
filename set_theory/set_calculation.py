from manim import *
class SetCalculation(Scene):
    def construct(self):
        # 创建集合A和B
        self.wait(0.5)
        circle = Circle(radius=1.2,color=WHITE, fill_opacity=0, stroke_color=WHITE, stroke_opacity=0.75)
        set_A = circle.copy().shift(LEFT * 2)
        set_B = circle.copy().shift(RIGHT * 2)
        text_a = Text(r"A", font_size=36).next_to(set_A, UP, buff=0.2)
        text_b = Text(r"B", font_size=36).next_to(set_B, UP, buff=0.2)
        self.play(Create(set_A), Create(set_B))
        self.play(FadeIn(text_a), FadeIn(text_b))
        self.wait(1)
        self.play(set_A.animate.set_opacity(0.5), set_B.animate.set_opacity(0.5))
        self.wait(1)

        # 集合间运算关系
        # 1）定义基础运算关系
        A = VGroup(set_A, text_a)
        B = VGroup(set_B, text_b)
        text_1_a = MathTex(r"A \cup B", font_size=48).move_to(DOWN * 1.5)
        text_1_b = MathTex(r"\bigcup_{i \in I} A_i", font_size=48).move_to(DOWN * 1.5)
        text_2_a = MathTex(r"A \cap B", font_size=48).move_to(DOWN * 1.5)
        text_2_b = MathTex(r"\bigcap_{i \in I} A_i", font_size=48).move_to(DOWN * 1.5)
        text_3_a = MathTex(r"A - B", font_size=48).move_to(DOWN * 1.5)
        text_3_b = MathTex(r"A \setminus B", font_size=48).next_to(text_3_a, DOWN)
        # 2）定义并集
        self.play(
            A.animate.shift(UP * 0.5),
            B.animate.shift(UP * 0.5),
            run_time=1
        )
        self.wait(0.5)
        self.play(FadeIn(text_1_a), run_time=1)
        self.wait(1)
        dots_1 = MathTex(r"\cdots", font_size=72, color=WHITE).move_to(UP * 0.5)
        self.play(FadeIn(dots_1), run_time=1)
        self.wait(0.5)
        self.play(Transform(text_1_a, text_1_b, run_time=2))
        self.wait(1)
        # 3）定义交集
        self.play(FadeOut(text_1_a, dots_1))
        self.wait(0.5)
        self.play(
            A.animate.shift(RIGHT * 1.25),
            B.animate.shift(LEFT * 1.25),
            run_time=1
        )
        self.wait(0.5)
        self.play(FadeIn(text_2_a), run_time=1)
        self.wait(1)
        dots_2 = MathTex(
            r"\cdots",
            font_size=72, color=WHITE).move_to(RIGHT * 3 + UP * 0.5)
        self.play(FadeIn(dots_2), run_time=1)
        self.wait(0.5)
        self.play(Transform(text_2_a, text_2_b, run_time=2))
        self.wait(1)
        # 4）定义差集
        self.play(FadeOut(text_2_a, dots_2))
        self.wait(0.5)
        B_border = set_B.copy().set_stroke(color=WHITE, opacity=0.75)
        B_border.set_fill(color=WHITE, opacity=0)
        difference = Difference(set_A, set_B, color=WHITE, fill_opacity=0.5)
        self.play(
            ReplacementTransform(VGroup(set_A, set_B), VGroup(difference, B_border)),
            run_time=2
        )
        self.wait(0.5)
        self.play(FadeIn(text_3_a), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(text_3_b), run_time=1)
        self.wait(1)

        # 清除所有对象
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

        # 交换律
        self.wait(0.5)
        text_title_a = Text(r"交换律", font_size=36).move_to(UP * 1.5)
        text_4_a = MathTex(
            r"A \cap ( B \cup C ) = (A \cap B) \cup (A \cap C)",
            font_size=48
            ).move_to(UP * 0.5)
        text_4_b = MathTex(
            r"A \cup (B \cap C) = (A \cup B) \cap (A \cup C)",
            font_size=48
            ).move_to(DOWN * 0.5)
        self.play(FadeIn(text_title_a), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(text_4_a, text_4_b), run_time=2)
        self.wait(1)
        # 德摩根律
        self.play(FadeOut(text_title_a, text_4_a, text_4_b))
        text_title_b = Text(r"德摩根律", font_size=36).move_to(UP * 1.5)
        text_5_a = MathTex(
            r"A - (B \cup C) = (A - B) \cap (A - C)",
            font_size=48
            ).move_to(UP * 0.5)
        text_5_b = MathTex(
            r"A - (B \cap C) = (A - B) \cup (A - C)",
            font_size=48
            ).move_to(DOWN * 0.5)
        self.wait(0.5)
        self.play(FadeIn(text_title_b), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(text_5_a, text_5_b), run_time=2)
        self.wait(1)

