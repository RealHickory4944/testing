import decimal
import time
import os

# Set precision for Decimal calculations
decimal.getcontext().prec = 10050  # a bit more than needed

SAVE_FILE = "pi.txt"

def compute_pi(precision):
    """Compute pi to the given precision using the Chudnovsky algorithm."""
    decimal.getcontext().prec = precision + 2
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
    return +pi  # apply precision

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

    # Compute pi once to high precision
    pi_str = str(compute_pi(10000))  # 10k digits
    pi_str = pi_str.replace(".", "")  # remove decimal point

    if n_digits == 0:
        print("3.", end="", flush=True)

    while n_digits < len(pi_str) - 1:
        next_digit = pi_str[n_digits + 1]  # +1 because index 0 is "3"
        print(next_digit, end="", flush=True)
        pi_digits += next_digit
        save_state(pi_digits)
        n_digits += 1
        time.sleep(0.1)  # slow down for readability

if __name__ == "__main__":
    main()
