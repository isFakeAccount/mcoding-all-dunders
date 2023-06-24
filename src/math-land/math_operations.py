from __future__ import annotations

from math import pi


class FixedPoint:
    def __init__(
        self,
        *,
        fixed_point_value: int,
        signed: bool,
        word_length: int,
        fraction_length: int,
    ):
        self.signed = signed
        self.word_length = word_length
        self.integer_length = word_length - fraction_length
        self.fraction_length = fraction_length
        self.fixed_point_value = fixed_point_value

    @classmethod
    def from_float(
        cls, value: float, word_length: int, fraction_length: int
    ) -> "FixedPoint":
        signed = value < 0

        min_range = cls.min_representable(signed, word_length, fraction_length)
        max_range = cls.max_representable(signed, word_length, fraction_length)

        if not (min_range <= value <= max_range):
            raise OverflowError(
                f"{value} is outside the valid range of the Fixed Point Datatype. "
                f"The allowed range is [{min_range}, {max_range}]."
            )

        # Shift fractional bits to the left of the binary point
        quantized_value = round(value * (1 << fraction_length))

        return cls(
            fixed_point_value=quantized_value,
            signed=value < 0,
            word_length=word_length,
            fraction_length=fraction_length,
        )

    @classmethod
    def from_int(
        cls, value: int, word_length: int, fraction_length: int
    ) -> "FixedPoint":
        # Shift fractional bits to the left of the binary point
        quantized_value = value << fraction_length
        return cls(
            fixed_point_value=quantized_value,
            signed=value < 0,
            word_length=word_length,
            fraction_length=fraction_length,
        )

    def __int__(self) -> int:
        return self.fixed_point_value >> self.fraction_length

    def __float__(self) -> float:
        return float(self.fixed_point_value / (1 << self.fraction_length))

    def __complex__(self) -> complex:
        return complex(self.__float__())

    def __repr__(self) -> str:
        return (
            f"Fixdt(value={self.__float__()}, signed={self.signed}, "
            f"word_length={self.word_length}, fraction_length={self.fraction_length})"
        )

    def __str__(self) -> str:
        return (
            f"Fixed Point: {self.__float__()}, Signed: {self.signed}, "
            f"Word Length: {self.word_length}, Fraction Length: {self.fraction_length}"
        )

    @staticmethod
    def max_representable(
        signed: bool, word_length: int, fraction_length: int
    ) -> float:
        """Maximum representable floating point number."""
        return float(
            int(2 ** (word_length - signed) - 1) * 2**-fraction_length
        )

    @staticmethod
    def min_representable(
        signed: bool, word_length: int, fraction_length: int
    ) -> float:
        """Minimum representable floating point number."""
        return float(
            int(2 ** (word_length - 1) * -signed) * 2**-fraction_length
        )


if __name__ == "__main__":
    print(f"PI from Maths Library: {pi}")

    neg_pi_fixdt = FixedPoint.from_float(-pi, 16, 13)
    print(f"{neg_pi_fixdt!r}: {neg_pi_fixdt!s}")
    print(
        f"Fixed Point Negative PI Converted back to Float: {float(neg_pi_fixdt)}"
    )
    print(f"Int part of Fixed Point: {int(neg_pi_fixdt)}")
    print(complex(neg_pi_fixdt))

    pos_pi_fixdt = FixedPoint.from_float(pi, 16, 14)
    print(f"{pos_pi_fixdt!r}: {pos_pi_fixdt!s}")
    print(f"Fixed Point PI Converted back to Float: {float(pos_pi_fixdt)}")
    print(f"Int part of Fixed Point: {int(pos_pi_fixdt)}")
