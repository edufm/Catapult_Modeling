# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:04:07 2016

@author: edufe
"""
import math
from scipy.integrate import odeint
from numpy import linspace


def Calculos(A, TB, VC, M, N):
    
    A = float(A)
    TB = float(TB)
    VC = float(VC)
    M = float(M)    
    N = float(N)
    
    Larg = 2.5           # dist entre braços de catapulta em M
    dX = 0.16            # Larg braço em M
    X = (Larg-dX)/2      # dist braço lateral

    p = 0.16             # Dist entre cordas
    c = 0.24             # Raio de rotação das cordas
    mc = 0.200*Larg        # Massa corda
    
    V = VC               # Numero de voltas
    Ka = 3.4 + (N*2.2)# Coeficiente de elasticidade da corda
    O = 0                # Angulo incial
    OF = (V)*(2*math.pi*(c/100)) # Angulo final
    
    J = mc*(dX*dX)       # Momento de inercia da corda
    
    ymax = (OF * c) / dX
    
    T = (c * ymax) / J
    
    TF = T * Ka

    l = TB           #Tamanho do braço
    PM = 1           #Peso do braço por metro
    Pb = TB*PM       #Peso do braço
    Teta = A         #Angulo de lançamento em rad
            
    m = M            #Massa pedra
    Dp = (M/5)       #Diamero pedra em g
    G = 9.8
    
    Torque = TF * l
    
    Fpb = ((1/2)*l)*Pb * G
    
    Fp = l * m * G
    
    Fr = Torque - (Fpb + Fp)
    
    if Fr <= 0:
        return [0, 0]
    
    Frx = Fr * math.sin(Teta)
    
    Fry = Fr * math.cos(Teta)
    
    lTeta = (Teta * math.pi * l)/180
    
    ENx = abs(Frx*lTeta)
    ENy = abs(Fry*lTeta)
    
    Vx0 = math.sqrt((ENx*2)/m)
    Vy0 = math.sqrt((ENy*2)/m)
    
    Dx0 = 0
    Dy0 = l+0.5
    
    Dar = 1.225
    Carrasto = 0.46
    AF = (math.pi * (Dp**2))/4

    Rar = (Dar*Carrasto*AF)/(2*(m*5))
    
    L = [Dx0, Vx0, Dy0, Vy0]
    
    t = linspace(0, 20, 201)
        
    def func1(Y, t):
        Vy = - (G * m) - ((Y[3]**2) * Rar)
        Vx = - ((Y[1]**2) * Rar)
        Dx = + (Y[1])
        Dy = + (Y[3])
    
        return[Dx, Vx, Dy, Vy]
    
    R = odeint(func1, L, t)
    
    LVx = []
    LVy = []
    LDx = []
    LDy = []
    for i in range (len(t)):
        if R[i][2] > 0:
            LDx.append(R[i][0])
            LVx.append(R[i][1])
            LDy.append(R[i][2])
            LVy.append(R[i][3])
    
    return[LDx, LDy]