from manim import *
class SetDefined(Scene):
    def construct(self):
        # 创建对象与元素
        objects = VGroup(*[Circle(radius=0.3, color=WHITE, fill_opacity=1) for _ in range(3)]).arrange(RIGHT, buff=0.5)
        elements = VGroup(*[Text(chr(ord('a')+i), font_size=36, color=WHITE) for i in range(3)])
        for obj, element in zip(objects, elements):
            element.next_to(obj, UP, buff=0.2)
        togeter = VGroup(objects, elements)
        # 创建动画
        animations_1 = [FadeIn(object) for object in objects]
        animations_2 = [FadeIn(element) for element in elements]
        self.play(Succession(*animations_1, lag_ratio=1.0))
        self.wait(1)
        self.play(Succession(*animations_2, lag_ratio=1.0))
        self.wait(1)
        self.play(togeter.animate.shift(UP*1.5))
        self.wait(1)

        # 定义集合
        # 1）
        left_part = MathTex(r"\{ a, b, c \}", font_size=48, color=WHITE)
        right_part = MathTex(r"= A", font_size=48, color=WHITE).next_to(left_part, RIGHT, buff=0.2)
        self.play(Write(left_part))
        self.wait(0.5)
        self.play(left_part.animate.shift(LEFT*0.5))
        self.wait(0.5)
        # 2）
        right_part.shift(LEFT*0.5)
        self.play(FadeIn(right_part))
        self.wait(0.5)
        combined = VGroup(left_part, right_part)
        defined = MathTex(r"A = \{ a, b, c \}", font_size=48, color=WHITE)
        self.play(Transform(combined, defined), run_time=1)
        # 3）
        relation = MathTex(r"a, b, c \in A", font_size=48, color=WHITE).next_to(defined, DOWN, buff=0.5)
        self.play(FadeIn(relation))
        self.wait(0.5)
        
        # 打包对象并移动
        self.play(FadeOut(left_part), FadeOut(right_part), FadeOut(relation))
        self.play(togeter.animate.shift(DOWN))
        self.wait(0.2)

        # 集合说明
        # 1）创建“盒子”
        rect = SurroundingRectangle(togeter, buff=0.5)
        self.play(Create(rect), run_time=2)
        self.wait(0.2)
        # 2）创建问题
        box = Text(r"盒子S", font_size=36).next_to(rect, UR, buff=0.2)
        text_q_1 = Text(r"小球a", font_size=36)
        text_q_2 = MathTex(r"\in", font_size=36)
        text_q_3 = Text(r"盒子S", font_size=36)
        text_q_4 = Text(r"?", font_size=48)
        question = VGroup(
            text_q_1, text_q_2, text_q_3, text_q_4
        ).arrange(RIGHT, buff=0.2).next_to(rect, DOWN, buff=0.5)
        question.shift(RIGHT*0.2)
        # 3）动画展示
        self.play(FadeIn(box))
        self.wait(0.5)
        self.play(FadeIn(question))
        self.wait(0.5)
        self.play(FadeOut(text_q_4))
        self.wait(0.2)
        not_in = MathTex(r"\notin", font_size=36).move_to(text_q_2.get_center())
        self.play(Transform(text_q_2, not_in), run_time=1)
        self.wait(0.5)

