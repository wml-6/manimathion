from manim import *
class Collection(Scene):
    def construct(self):
        # 显示对象与元素
        objects = VGroup(*[Circle(radius=0.3, color=GRAY, fill_opacity=1) for _ in range(3)]).arrange(RIGHT, buff=0.5)
        elements = VGroup(*[Text(chr(ord('a')+i), font_size=24, color=WHITE) for i in range(3)])
        for obj, element in zip(objects, elements):
            element.next_to(obj, UP, buff=0.2)
        combined = VGroup(objects, elements)

        animations_1 = [FadeIn(object) for object in objects]
        animations_2 = [FadeIn(element) for element in elements]
        
        self.play(Succession(*animations_1, lag_ratio=1.0))
        self.wait(1)
        self.play(Succession(*animations_2, lag_ratio=1.0))
        self.wait(1)
        self.play(combined.animate.shift(UP*1.5))
        self.wait(1)

        # 显示表达式
        left_part = MathTex(r"\{ a, b, c \}", font_size=48, color=WHITE)
        right_part = MathTex(r"= A", font_size=48, color=WHITE).next_to(left_part, RIGHT, buff=0.2)

        self.play(Write(left_part))
        self.wait(0.5)
        self.play(left_part.animate.shift(LEFT*0.5))
        self.wait(0.5)

        right_part.shift(LEFT*0.5)
        self.play(Write(right_part))
        self.wait(0.5)

        relation = MathTex(r"a, b, c \in A", font_size=48, color=WHITE).next_to(left_part, DOWN, buff=0.5)
        relation.shift(RIGHT*0.8)
        self.wait(0.5)
        self.play(Write(relation))
        self.wait()
        
        