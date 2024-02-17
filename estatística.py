#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 11:51:57 2023

@author: Elaine Cecília Gatto - Cissa
"""


import numpy
import statistics
import collections

# https://docs.python.org/pt-br/3/library/statistics.html 

# definindo um vetor
sequencia = [200, 201, 200, 202, 203, 204, 205, 204, 204, 205, 202, 200, 200, 206, 207, 208, 209, 207, 207, 208]
print(sequencia)

# tamanho do vetor
m = len(sequencia)
print(m)

# soma
soma = sum(sequencia)
print(soma)

# multiplicacao
multiplicacao = numpy.prod(sequencia)
print(multiplicacao)

# raiz quadrada
raiz_quadrada = numpy.sqrt(sequencia)
print(raiz_quadrada)

# potencia de 2
potencia_2 = numpy.power(sequencia,2)
print(potencia_2)

# potencia de 5
potencia_5 = numpy.power(sequencia,5)
print(potencia_5)

# valor máximo
maximo = numpy.max(sequencia)
print(maximo)

# valor mínimo
minimo = numpy.min(sequencia)
print(minimo)

# desvio padrão
dp = numpy.std(sequencia)
print(dp)

dp_populacional = statistics.pstdev(sequencia)
print(dp_populacional)

dp_amostral = statistics.stdev(sequencia)
print(dp_amostral)

# 25%
percentil_25 = numpy.percentile(sequencia, 25)
print(percentil_25)

# 50%
percentil_50 = numpy.percentile(sequencia, 50)
print(percentil_50)

# 75%
percentil_75 = numpy.percentile(sequencia, 75)
print(percentil_75)

# quartis 
quartis = statistics.quantiles(sequencia)
print(quartis)

# frequencia 
frequencia = collections.Counter(sequencia)
print(frequencia)

# amplitude
amplitude = maximo - minimo
print(amplitude)

# ponto médio
ponto_medio = (maximo+minimo)/2
print(ponto_medio)

# moda
moda = statistics.mode(sequencia)
print(moda)

# média ponderada
media_ponderada = numpy.average(sequencia)
print(media_ponderada)

# mediana
mediana_1 = numpy.median(sequencia)
print(mediana_1)

mediana_2 = statistics.median(sequencia)
print(mediana_2)

# média aritmética
media_aritmetica_1 = numpy.mean(sequencia)
print(media_aritmetica_1)

media_aritmetica_2 = statistics.mean(sequencia)
print(media_aritmetica_2)

# média quadrática
media_quadratica = numpy.sqrt(sum(potencia_2)/m)
print(media_quadratica)

# média geométrica
media_geometrica_1 = numpy.power(abs(multiplicacao), (1/4))
print(media_geometrica_1)

media_geometrica_2 = statistics.geometric_mean(sequencia)
print(media_geometrica_2)

# média harmônica
media_harmonica = statistics.harmonic_mean(sequencia)
print(media_harmonica)

# diferencial interquantil
di = percentil_75 - percentil_25
print(di)

# limites
limite_inferior = percentil_25 - (1.5*di)
print(limite_inferior)

limite_superior = percentil_75 - (1.5*di)
print(limite_superior)

# variância
variancia_amostral = statistics.variance(sequencia)
print(variancia_amostral)

variancia_populacional = statistics.pvariance(sequencia)
print(variancia_populacional)

variancia_1 = numpy.var(sequencia)
print(variancia_1)

# coeficiente de variação
cv = dp/media_aritmetica_1
print(cv)

