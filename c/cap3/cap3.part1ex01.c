/* Copyright (C) 2022-2023 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book:
 * https://editora.ufabc.edu.br/matematica-e-ciencias-da-computacao/58-processando-a-informacao
 * Language: C
 */

#include <stdio.h>
#include <math.h>

 // MÉTODOS
float delta(float a, float b, float c) {
  float d = b * b - 4 * a * c;
  return d;
}

float leia() {
  float valor;
  printf("Entre com um valor: ");
  scanf("%f", &valor);
  return valor;
}

// PROGRAMA PRINCIPAL
int main(void) {

  // ENTRADAS
  float a, b, c;
  a = leia();
  b = leia();
  c = leia();

  // PROCESSAMENTO e SAÍDA
  double d = (double)delta(a, b, c);
  printf("Delta = %.1f\n", d);
  if (d < 0) {
    printf("A equacao nao possui rai4zes reais\n");
  }
  if (d == 0) {
    printf("Raiz 1: %.1f\n", (-b + sqrt(d) / 2 * a));
  }
  if (d > 0) {
    printf("Raiz 2: %.1f e %.1f\n", (-b - sqrt(d) / 2 * a), (-b + sqrt(d) / 2 * a));
  }
  return 0;
}