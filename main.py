from manim import *
from set_theory.set_defined import SetDefined
from set_theory.set_illustration import SetIllustration
from set_theory.set_calculation import SetCalculation
from set_theory.set_family import SetFamily

if __name__ == "__main__":
    # 直接渲染场景
    scene_1 = SetDefined()
    scene_2 = SetIllustration()
    scene_3 = SetCalculation()
    scene_4 = SetFamily()
    scene_4.render()