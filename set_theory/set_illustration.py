from manim import *
class SetIllustration(Scene):
    def construct(self):
        # 创建集合X和点x
        X = Circle(radius=1.5, color=WHITE, fill_opacity=0)
        x = Dot(color=WHITE, radius=0.1)
        text_X = Text(r"X", font_size=36).next_to(X, UR, buff=0)
        text_x = Text(r"x", font_size=36).next_to(x, UR, buff=0.1)
        self.play(Create(X))
        self.wait(0.2)
        self.play(FadeIn(text_X))
        self.wait(0.5)
        self.play(FadeIn(x), FadeIn(text_x))
        self.wait(1)

        # 创建集合A和B
        self.play(FadeOut(text_X), FadeOut(text_x), FadeOut(x))
        small_X = Circle(radius=1.2, color=WHITE, fill_opacity=0)
        self.play(Transform(X, small_X), run_time=1)
        set_A = small_X.copy().shift(LEFT * 2)
        set_B = small_X.copy().shift(RIGHT * 2)
        self.play(Transform(X, set_A), run_time=1)
        text_a1 = Text(r"A", font_size=36).next_to(set_A, UP, buff=0.2)
        text_b1 = Text(r"B", font_size=36).next_to(set_B, UP, buff=0.2)
        self.play(FadeIn(set_A))
        self.play(FadeOut(X))
        self.play(FadeIn(text_a1))
        self.play(Create(set_B), run_time=1)
        self.play(FadeIn(text_b1))
        self.wait(0.5)

        # 集合间包含关系
        # 1）建立包含关系
        self.play(FadeOut(text_a1), FadeOut(text_b1))
        small_A = Circle(radius=0.4, color=WHITE, fill_opacity=0).shift(LEFT * 2)
        self.play(Transform(set_A, small_A), run_time=0.5)
        self.play(
            set_A.animate.shift(RIGHT * 2.1), 
            set_B.animate.shift(LEFT * 2.1),
            run_time=0.5
            )
        text_a2 = Text(r"A", font_size=36).next_to(set_A, UL, buff=0)
        text_b2 = Text(r"B", font_size=36).next_to(set_B, UR, buff=0)
        self.play(FadeIn(text_a2), FadeIn(text_b2))
        self.wait(0.5)
        # 2）定义包含关系
        contain_1 = VGroup(set_A, set_B, text_a2, text_b2)
        self.play(contain_1.animate.shift(LEFT * 2))
        contain_1_copy = contain_1.copy()
        text_1_a = MathTex(r"A \subset B", font_size=48).next_to(contain_1, RIGHT, buff=1.5).shift(UP * 0.25)
        text_1_b = MathTex(r"B \supset A", font_size=48).next_to(text_1_a, DOWN, buff=0.5)
        self.play(AnimationGroup(
            FadeIn(text_1_a),
            FadeIn(text_1_b),
            lag_ratio=0.5,
            run_time=2
            ))
        self.wait(1)
        # 3）定义相等关系
        self.play(FadeOut(text_1_a), FadeOut(text_1_b))
        self.wait(0.5)
        self.play(FadeOut(text_a2))
        self.wait(0.5)
        self.play(Transform(set_A, set_B, run_time=1))
        text_a3 = Text(r"A", font_size=36).next_to(set_A, UL, buff=0)
        self.play(FadeIn(text_a3))
        self.wait(0.5)
        text_2_a = MathTex(r"""
                         \begin{cases}
                         A \subset B \\
                         A \supset B 
                         \end{cases}
                         """,
                         font_size=48).next_to(set_A, RIGHT, buff=1.5)
        text_2_b = MathTex(r"A = B", font_size=48).next_to(set_A, RIGHT, buff=1.5)
        self.play(FadeIn(text_2_a))
        self.wait(1)
        self.play(Transform(text_2_a, text_2_b, run_time=2))
        self.wait(1)
        # 4）定义真子集
        contain_2 = VGroup(set_A, set_B, text_a3, text_b2)
        self.play(FadeOut(text_2_a))
        self.play(Transform(contain_2, contain_1_copy, run_time=1))
        self.wait(0.5)
        text_3_a = MathTex(r"""
                         \begin{cases}
                         A \subset B\\
                         and\\
                         A \neq B
                         \end{cases}
                         """,
                         font_size=48).next_to(contain_2, RIGHT, buff=1.5)
        text_3_b = MathTex(r"A \subsetneq B", font_size=48).next_to(contain_2, RIGHT, buff=1.5)
        self.play(FadeIn(text_3_a))
        self.wait(1)
        self.play(Transform(text_3_a, text_3_b, run_time=2))
        self.wait(1)
        # 5）定义子集
        self.play(FadeOut(text_3_a))
        text_4_a = MathTex(r"""
                         \begin{cases}
                         A \subsetneq B\\
                         or\\
                         A = B
                         \end{cases}
                         """, font_size=48).next_to(contain_2, RIGHT, buff=1.5)
        text_4_b = MathTex(r"A \subseteq B", font_size=48).next_to(contain_2, RIGHT, buff=1.5)
        self.play(FadeIn(text_4_a))
        self.wait(1)
        self.play(Transform(text_4_a, text_4_b, run_time=2))
        self.wait(1)
        # 6）定义空集
        self.play(FadeOut(text_4_a))
        text_5_a = MathTex(r"A =", font_size=48).next_to(set_B, RIGHT, buff=1.5)
        text_5_b = MathTex(
                            r"\varnothing",
                            font_size=48
                            ).next_to(text_5_a, RIGHT, buff=0.2).shift(DOWN * 0.05)
        self.wait(0.5)
        self.play(ShrinkToCenter(set_A), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(VGroup(text_5_a, text_5_b)))
        self.wait(0.5)
        self.play(FadeOut(text_5_a))
        self.wait(0.5)
        self.play(text_5_b.animate.shift(LEFT * 1.2))
        self.wait(0.5)
        text_5_c = MathTex(
                            r"\subset", r"X",
                            font_size=48
                            ).next_to(text_5_b, RIGHT, buff=0.2).shift(UP * 0.02)
        self.play(FadeIn(text_5_c))
        self.wait(1)
