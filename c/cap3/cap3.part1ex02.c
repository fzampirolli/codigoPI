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

 // MÉTODO
float leia() {
  float valor;
  printf("Entre com um valor: ");
  scanf("%f", &valor);
  return valor;
}

// PROGRAMA PRINCIPAL
int main(void) {

  // ENTRADAS
  float nota1 = leia();
  float nota2 = leia();

  // PROCESSAMENTO E SAÍDA
  float media = (nota1 + nota2) / 2;
  if (media >= 9.0)
    printf("Conceito A\n");
  else if (media >= 7.5)
    printf("Conceito B\n");
  else if (media >= 6.0)
    printf("Conceito C\n");
  else if (media >= 5.0)
    printf("Conceito D\n");
  else
    printf("Reprovado! Conceito F\n");
  return 0;
}