import decimal
import time
import os

# How many digits to compute in one batch
PRECISION = 2000
decimal.getcontext().prec = PRECISION + 5

SAVE_FILE = "pi_digits.txt"

def compute_pi(precision):
    """Compute pi using the Chudnovsky algorithm."""
    decimal.getcontext().prec = precision + 5
    C = 426880 * decimal.Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L
    for i in range(1, precision):
        M = (K**3 - 16*K) * M // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12
    pi = C / S
    return +pi

def load_state():
    """Load previously saved digits if available."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = f.read().strip()
            return len(data) - 2, data  # exclude "3."
    return 0, "3."

def save_state(pi_digits):
    """Save current digits to file."""
    with open(SAVE_FILE, "w") as f:
        f.write(pi_digits)

def main():
    n_digits, pi_digits = load_state()

    while True:
        # Compute a fresh batch of digits
        pi_str = str(compute_pi(PRECISION)).replace(".", "")

        # If starting fresh, print "3."
        if n_digits == 0:
            print("3.", end="", flush=True)

        # Output digits one by one
        while n_digits < len(pi_str) - 1:
            next_digit = pi_str[n_digits + 1]  # +1 skips the "3"
            print(next_digit, end="", flush=True)
            pi_digits += next_digit
            save_state(pi_digits)  # write after every digit
            n_digits += 1
            time.sleep(0.05)  # slow down for readability

        # Once we exhaust this batch, increase precision and continue
        PRECISION += 1000
        decimal.getcontext().prec = PRECISION + 5

if __name__ == "__main__":
    main()
