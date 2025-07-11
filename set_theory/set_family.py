from manim import *
class SetFamily(Scene):
    def construct(self):
        # 创建对象
        # 1）创建点
        dot = Dot(color=WHITE)
        text_dot = Text(r"a", font_size=24, color=WHITE).next_to(dot, UR, buff=0)
        self.play(FadeIn(dot), FadeIn(text_dot))
        self.wait(0.5)
        # 2）创建集合
        set = Circle(radius=0.5, color=WHITE, fill_opacity=0, stroke_color=WHITE, stroke_opacity=1)
        text_set = Text(r"A", font_size=36, color=WHITE).next_to(set, UR, buff=0)
        self.play(Create(set), FadeIn(text_set))
        self.wait(0.5)
        # 3）创建集族
        family = Circle(radius=2., color=WHITE, fill_opacity=0, stroke_color=WHITE, stroke_opacity=1)
        text_family = MathTex(r"\mathcal{A}", font_size=48, color=WHITE).next_to(family, UR, buff=0)
        self.play(Create(family), FadeIn(text_family))
        self.wait(0.5)
        # 4）创建集族的元素
        self.play(FadeOut(dot), FadeOut(text_dot))
        set_copy_1 = set.copy().shift(LEFT * 0.5).scale(0.75)
        set_copy_2 = set.copy().shift(RIGHT).scale(0.5)
        text_set_1 = MathTex(r"A_1", font_size=24).next_to(set_copy_1, UL, buff=0)
        text_set_2 = MathTex(r"A_2", font_size=24).next_to(set_copy_2, UR, buff=0)
        dots = MathTex(r"\cdots", font_size=72, color=WHITE).next_to(set, DOWN, buff=0.5)
        self.play(FadeIn(set_copy_1), FadeIn(set_copy_2))
        self.wait(0.5)
        self.play(FadeIn(text_set_1), FadeIn(text_set_2))
        self.wait(0.5)
        self.play(FadeIn(dots))
        self.wait(0.5)
        
        # 幂集
        # 1）打包对象并移动
        self.play(VGroup(
            set, set_copy_1, set_copy_2, text_set, text_set_1, text_set_2, dots, family, text_family
            ).animate.shift(LEFT * 2))
        self.wait(0.5)
        # 2）定义幂集
        text_1_a = MathTex(r"""
                         \begin{cases}
                         A_1 \subset A \\
                         A_2 \subset A \\
                         \cdots \subset A \\
                         A_n \subset A
                         \end{cases}
                         """,
                         font_size=48, color=WHITE).move_to(RIGHT * 2)
        text_1_b = MathTex(
                                r"\mathcal{A} = \mathcal{P} (A)",
                                font_size=48, color=WHITE
                                ).move_to(RIGHT * 2)
        self.play(FadeIn(text_1_a))
        self.wait(1)
        self.play(Transform(text_1_a, text_1_b, run_time=2))
        self.wait(1)

        # 清除所有对象
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])

        # 笛卡儿积
        # 1）创建集合A，B
        self.wait(0.5)
        circle = Circle(radius=1.2,color=WHITE, fill_opacity=0, stroke_color=WHITE, stroke_opacity=0.75)
        set_A = circle.copy().shift(LEFT * 2)
        set_B = circle.copy().shift(RIGHT * 2)
        text_a = Text(r"A", font_size=36).next_to(set_A, UP, buff=0.2)
        text_b = Text(r"B", font_size=36).next_to(set_B, UP, buff=0.2)
        self.play(Create(set_A), Create(set_B))
        self.play(FadeIn(text_a), FadeIn(text_b))
        self.wait(1)
        # 2）创建集合中元素
        dot_a = Dot(color=WHITE).move_to(LEFT * 2.5)
        dot_b = Dot(color=WHITE).move_to(RIGHT * 1.5)

        