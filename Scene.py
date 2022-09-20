from manim import *
import random

class RandomThings(Scene):
    def construct(self):
        block_zero = VGroup(
            Square(
                fill_opacity=1,
                fill_color=WHITE
            ),
            Tex(
                "0",
                color = BLACK
            ).scale(2)
        )
        block_one = VGroup(
            Square(
                fill_opacity=0
            ),
            Tex("1").scale(2)
        )

        title = Title("Number: ")

        block_one.next_to(block_zero, RIGHT)
        VGroup(block_zero, block_one).center()

        blocks = [block_zero, block_one]

        self.add(block_zero, block_one, title)
        self.wait()

        title_string = ""

        title.add_updater(lambda x: x.become(Title(f"Number: {title_string}")))

        for i in range(15):
            number = random.randint(0, len(blocks)-1)
            self.play(Indicate(blocks[number]))
            title_string = str(number) + title_string

class Base10Anim(Scene):
    def construct(self):

        def CreateNumberBlock(number: int, dark: bool = False):
            if dark:
                return VGroup(
                    Square(fill_color=WHITE, fill_opacity=1),
                    Tex(f"{number}", color=BLACK).scale(2)
                )
            else:
                return VGroup(
                    Square(fill_opacity=1, fill_color=DARKER_GRAY),
                    Tex(f"{number}").scale(2)
                )

        runningNum = 0

        blocks = [CreateNumberBlock(number) for number in range(1, 10)]

        blocks[1].next_to(blocks[0], RIGHT)
        blocks[2].next_to(blocks[1], RIGHT)

        blocks[3].next_to(blocks[0], DOWN)
        blocks[4].next_to(blocks[3], RIGHT)
        blocks[5].next_to(blocks[4], RIGHT)

        blocks[6].next_to(blocks[3], DOWN)
        blocks[7].next_to(blocks[6], RIGHT)
        blocks[8].next_to(blocks[7], RIGHT)

        blocksGroup = VGroup(*blocks).center().scale(0.75)

        anims = [FadeIn(block, shift=UP) for block in blocks]
        self.play(LaggedStart(*anims))

        """
        for i in range(5):
            randNum = random.randint(0, len(blocks)-1)
            runningNum += randNum
            self.play(Indicate(blocks[randNum]))
        """
        anims = [block.animate.scale(0.5) for block in blocks]
        self.play(LaggedStart(*anims))
        self.play(LaggedStart(*[block.animate.scale(2) for block in blocks]))
        self.play(LaggedStart(*[block.animate.shift(LEFT*3) for block in blocks]))
        self.play(LaggedStart(*[block.animate.shift(RIGHT*3) for block in blocks]))
        self.play(LaggedStart(*[Indicate(block, scale_factor=1.1) for block in blocks], lag_ratio=0.2))
        self.play(LaggedStart(*[block.animate.center() for block in blocks]))
        self.play(LaggedStart(*[FadeOut(block, shift=DOWN) for block in blocks]))

