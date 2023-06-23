from __future__ import annotations

from math import pi


class FixedPoint:
    def __init__(
        self,
        fixed_point_value: float,
        signed: bool,
        word_length: int,
        fraction_length: int,
    ):
        self.signed = signed
        self.word_length = word_length
        self.fraction_length = fraction_length
        self.fixed_point_value = fixed_point_value

    @classmethod
    def from_float(
        cls, value: float, signed: bool, word_length: int, fraction_length: int
    ) -> "FixedPoint":
        scale_factor = 2**fraction_length
        quantized_value = round(value * scale_factor)

        return cls(quantized_value, signed, word_length, fraction_length)

    def __int__(self) -> int:
        if self.signed:
            max_value = (1 << (self.word_length - 1)) - 1
            min_value = -(1 << (self.word_length - 1))
        else:
            max_value = (1 << self.word_length) - 1
            min_value = 0

        value = max(min(self.fixed_point_value, max_value), min_value)
        integer_part = value >> self.fraction_length
        return int(integer_part)

    def __float__(self) -> float:
        return float(self.fixed_point_value / (2**self.fraction_length))

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


if __name__ == "__main__":
    print(f"PI from Maths Library: {pi}")

    pi_fixdt = FixedPoint.from_float(pi, False, 16, 14)
    print(f"{pi_fixdt!r}: {pi_fixdt!s}")
    print(f"Fixed Point PI Converted back to Float: {float(pi_fixdt)}")
    print(f"Int part of Fixed Point PI: {int(pi_fixdt)}")
