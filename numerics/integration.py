"""
title:          Numerical Integration
version:        0.3.0
fileName:       Integration.py 
author:         Joachim Nilsen Grimstad

description:    Collection of some numerical integration routines. 
                
license:        GNU General Public License v3.0   
                
disclaimer:     For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software.
    
Todos:          Look into the Scipy integration libary?

""" 

def integrate_composite_trapezoidal_rule(func, lower_limit, upper_limit, n):
    # Composite trapezodial rule
    dx = (upper_limit - lower_limit) / n
    I = 0
    for k in range(0,n):
        step_lower_limit = lower_limit + (dx * k)
        step_upper_limit = lower_limit + (dx * (k + 1))
        I += (step_upper_limit - step_lower_limit) * ((func(step_lower_limit) + func(step_upper_limit)) / 2)
    return I

def integrate_composite_midpoint_rule(func, lower_limit, upper_limit, n):
    # Composite midpoint rule
    dx = (upper_limit - lower_limit) / n
    I = 0
    for k in range(0,n):
        step_lower_limit = lower_limit + (dx * k)
        step_upper_limit = lower_limit + (dx * (k + 1))
        I += (step_upper_limit - step_lower_limit) * func((step_lower_limit + step_upper_limit) / 2)
    return I

def integrate_composite_simpsons_rule(func, lower_limit, upper_limit, n):
    # Composite simpson's rule
    dx = (upper_limit - lower_limit) / n
    I = func(lower_limit)
    for k in range(1, n):
        if k % 2 == 0:
            I += 2 * func(lower_limit + (dx * k))
        else:
            I += 4 * func(lower_limit + (dx * k))
    I += func(upper_limit)
    I = dx * ( I / 3)
    return I 

if __name__ == '__main__':
    from timeit import default_timer as timer

    def test_function(x):
        return x**2 + 5*x

    # Numerical integration parameters
    lower_limit = 0
    upper_limit = 10
    n = 20

    # Composite midpoint rule
    midpoint_start = timer()
    midpoint_rule = integrate_composite_midpoint_rule(test_function, lower_limit, upper_limit, n)
    midpoint_end = timer()

    # Composite trapezodial rule 
    trapezodial_start = timer()
    trapezodial_rule = integrate_composite_trapezoidal_rule(test_function, lower_limit, upper_limit, n)
    trapezodial_end = timer()

    # Composite simpson's rule
    simpsons_start = timer()
    simpsons_rule = integrate_composite_simpsons_rule(test_function, lower_limit, upper_limit, n)
    simpsons_end = timer()

    # Evaluation
    print(f'Composite midpoint rule with integration limit from {lower_limit} to {upper_limit} gives {midpoint_rule} after {(midpoint_end - midpoint_start):.3} seconds')
    print(f'Composite trapezodial rule with integration limit from {lower_limit} to {upper_limit} gives {trapezodial_rule} after {(trapezodial_end - trapezodial_start):.3} seconds')
    print(f"Composite simpson's rule with integration limit from {lower_limit} to {upper_limit} gives {simpsons_rule} after {(simpsons_end - simpsons_start):.3} seconds")
    print('Exact answer to test_function from 0 to 10, is 583.33...')