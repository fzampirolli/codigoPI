/* Copyright (C) 2022 Francisco de Assis Zampirolli - All Rights Reserved
 * Author: Francisco de Assis Zampirolli
 * Purpose: Examples and some exercises from the Information Processing book
 * Language: C
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>5.
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