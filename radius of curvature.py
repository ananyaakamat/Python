from sympy import symbols, cos, diff, pi
r, t = symbols('r t')
r_expr = 4 * (1 + cos(t))
r1 = diff(r_expr, t)
r2 = diff(r_expr, t, t)
rho = (r_expr**2 + r1**2)**1.5 / (r_expr**2 + 2*r1**2 - r_expr*r2)
rho1 = rho.subs(t, pi/2).evalf()
print("The radius of curvature is %0.3f units" %rho1)
