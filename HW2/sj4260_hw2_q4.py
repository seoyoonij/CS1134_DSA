# Infinite series expansion of e
# Runtime = theta(n)

def e_approx(n):
    fact = 1
    e_series = 1.0
    for i in range(1, n+1):
        fact *= i # factorial, 
        e_series += 1/fact # add every time factorial is calculated for theta(n)
    return e_series


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx) # 15 deicimal places
        print("n = ", n, "Approximation: ", approx_str)

main()