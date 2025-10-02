import signal
import sys
import time

pi_estimate = 0.0
iterations = 0
sign = 1

def save_result():
    with open("pi.txt", "w") as f:
        f.write(f"Pi approximation after {iterations} iterations: {pi_estimate}\n")
    print(f"Saved π ≈ {pi_estimate} after {iterations} iterations")

def calculate_pi():
    global pi_estimate, iterations, sign
    while True:
        pi_estimate += sign * (4.0 / (2 * iterations + 1))
        iterations += 1
        sign *= -1
        if iterations % 1_000_000 == 0:
            save_result()
        time.sleep(0.000001)

def handle_stop(signum, frame):
    print("\nStopping workflow...")
    save_result()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_stop)
signal.signal(signal.SIGTERM, handle_stop)

if __name__ == "__main__":
    calculate_pi()
