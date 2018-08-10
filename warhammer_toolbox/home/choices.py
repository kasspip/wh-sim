
class DiceRequirement(object):
    NONE = "0"
    ONE_PLUS = "1"
    TWO_PLUS = "2"
    THREE_PLUS = "3"
    FOUR_PLUS = "4"
    FIVE_PLUS = "5"
    SIX_PLUS = "6"

    CHOICES = [
        (NONE, "-"),
        (ONE_PLUS, "1+"),
        (TWO_PLUS, "2+"),
        (THREE_PLUS, "3+"),
        (FOUR_PLUS, "4+"),
        (FIVE_PLUS, "5+"),
        (SIX_PLUS, "6+"),
    ]
