class DiceSuccessEnum(object):
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


class NumericalEnum(object):
    ZERO = "0"
    OME = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    ELVEN = "11"
    TWELVE = "12"

    CHOICES = [
        (ZERO, "-"),
        (OME, OME),
        (TWO, TWO),
        (THREE, THREE),
        (FOUR, FOUR),
        (FIVE, FIVE),
        (SIX, SIX),
        (SEVEN,SEVEN),
        (EIGHT, EIGHT),
        (NINE, NINE),
        (TEN, TEN),
        (ELVEN, ELVEN),
        (TWELVE, TWELVE),
    ]


class ExtendedNumericalEnum(object):
    THIRTEEN = '13'
    FOURTEEN = '14'
    FIFTEEN = '15'
    SIXTEEN = '16'
    SEVENTEEN = '17'
    EIGHTEEN = '18'
    NINETEEN = '19'
    TWENTY = '20'
    TW_ONE = '21'
    TW_TWO = '22'
    TW_THREE = '23'
    TW_FOUR = '24'
    TW_FIVE = '25'
    TW_SIX = '26'
    TW_SEVEN = '27'
    TW_EIGHT = '28'
    TW_NINE = '29'
    THIRTY = '30'

    CHOICES = [
        (THIRTEEN, THIRTEEN),
        (FOURTEEN, FOURTEEN),
        (FIFTEEN, FIFTEEN),
        (SIXTEEN, SIXTEEN),
        (SEVENTEEN, SEVENTEEN),
        (EIGHTEEN, EIGHTEEN),
        (NINETEEN, NINETEEN),
        (TWENTY, TWENTY),
        (TW_ONE, TW_ONE),
        (TW_TWO, TW_TWO),
        (TW_THREE, TW_THREE),
        (TW_FOUR, TW_FOUR),
        (TW_FIVE, TW_FIVE),
        (TW_SIX, TW_SIX),
        (TW_SEVEN, TW_SEVEN),
        (TW_EIGHT, TW_EIGHT),
        (TW_NINE, TW_NINE),
        (THIRTY, THIRTY),
    ]


class DiceEnum(object):
    ONE_D_THREE = "D3"
    TWO_D_THREE = "2D3"
    THREE_D_THREE = "3D3"
    ONE_D_SIX = "D6"
    TWO_D_SIX = "2D6"
    THREE_D_SIX = "3D6"

    CHOICES = [
        (ONE_D_THREE, ONE_D_THREE),
        (TWO_D_THREE, TWO_D_THREE),
        (THREE_D_THREE, THREE_D_THREE),
        (ONE_D_SIX, ONE_D_SIX),
        (TWO_D_SIX, TWO_D_SIX),
        (THREE_D_SIX, THREE_D_SIX),
    ]


class SpecialEnum(object):
    SPECIAL = '*'

    CHOICES = [
        (SPECIAL, SPECIAL),
    ]


class NumericalDiceEnum(NumericalEnum, DiceEnum):
    CHOICES = NumericalEnum.CHOICES + DiceEnum.CHOICES


class LargeNumericalEnum(NumericalEnum, ExtendedNumericalEnum):
    CHOICES = NumericalEnum.CHOICES + ExtendedNumericalEnum.CHOICES


class DegressiveNumericalEnum(NumericalEnum, SpecialEnum):
    CHOICES = SpecialEnum.CHOICES + NumericalEnum.CHOICES


class DegressiveDiceSuccessEnum(DiceSuccessEnum, SpecialEnum):
    CHOICES = SpecialEnum.CHOICES + DiceSuccessEnum.CHOICES


class DegressiveNumericalDiceEnum(NumericalEnum, DiceEnum, SpecialEnum):
    CHOICES = SpecialEnum.CHOICES + NumericalEnum.CHOICES + DiceEnum.CHOICES


class DegressiveLargeNumericalEnum(NumericalEnum, ExtendedNumericalEnum, SpecialEnum):
    CHOICES = SpecialEnum.CHOICES + NumericalEnum.CHOICES + ExtendedNumericalEnum.CHOICES
