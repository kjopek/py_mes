#!/usr/bin/env python

class Element:
    def __init__(self, mes, i, j):
        self.i, self.j = i, j
        self.mes = mes
        self.a, self.b, self.c, self.d = mes.ij_to_abcd(i,j)
        self.coeff = [null]*9
    
    def calculate_a(self):
        self.coeff[0] = mes.bitmap_value(a,c)
        self.coeff[1] = mes.bitmap_value(b,c)
        self.coeff[2] = mes.bitmap_value(c,d)
        self.coeff[3] = mes.bitmap_value(a,d)
        
    
    def calculate_b(self):
        f5 = lambda x: (mes.bitmap_derivative_x(x, c) - (self.coeff[0] * shift_me_baby(df_dx[0], a, b, c, d)(x, c) + self.coeff[1] * shift_me_baby(df_dx[1], a, b, c, d)(x, c) + self.coeff[2] * shift_me_baby(df_dx[2], a, b, c, d)(x, c) + self.coeff[3] * shift_me_baby(df_dx[3], a, b, c, d)(x, c))*shift_me_baby(functions[5], a, b, c, d)(x, c)
        
        self.coeff[5] = scipy.integrate.quadrature(f5, a, b)
            