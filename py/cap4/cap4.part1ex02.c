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

float lerNota(float acumulador, int n) {
  float nota = 0;
  if (n > 0) { // CRITÉRIO DE PARADA
    do {
      scanf("%f", &nota);
    } while (nota < 0.0 || nota > 10.0);
    acumulador = lerNota(acumulador, n - 1); // CHAMADA RECURSIVA,
    // ALTERAÇÃO DO VALOR DO ARGUMENTO !!!
  }
  return acumulador + nota;
}

int main(void) {

  // ENTRADA DE DADOS e PROCESSAMENTO
  float acumulador = 0, media;
  int contador = 10;

  printf("Entre com %d notas válidas\n", contador);
  acumulador = lerNota(acumulador, contador);
  media = acumulador / contador;

  // SAÍDA
  printf("A média das %d notas é %.1f\n", contador, media);

  return 0;
}