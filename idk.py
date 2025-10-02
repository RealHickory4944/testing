import signal
import sys
import time

# Global variable to store pi approximation
pi_estimate = 0.0
iterations = 0

def calculate_pi():
    """Approximate pi using the Leibniz series."""
    global pi_estimate, iterations
    pi_estimate = 0.0
    iterations = 0
    sign = 1
    while True:
        pi_estimate += sign * (4.0 / (2 * iterations + 1))
        iterations += 1
        sign *= -1
        if iterations % 1_000_000 == 0:
            print(f"Iteration {iterations}, π ≈ {pi_estimate}")
        time.sleep(0.000001)  # tiny sleep to avoid hogging CPU

def save_and_exit(signum, frame):
    """Save pi estimate to file when workflow is stopped."""
    print(f"\nStopping workflow... Saving π ≈ {pi_estimate} after {iterations} iterations.")
    with open("pi.txt", "w") as f:
        f.write(f"Pi approximation after {iterations} iterations: {pi_estimate}\n")
    sys.exit(0)

# Register signal handlers for manual stop
signal.signal(signal.SIGINT, save_and_exit)   # Ctrl+C
signal.signal(signal.SIGTERM, save_and_exit) # GitHub Actions stop

if __name__ == "__main__":
    calculate_pi()
