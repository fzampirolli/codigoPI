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
int main() {
  float area;
  int num;
  char escolha;
  printf("1. Circulo\n");
  printf("2. Quadrado\n");
  printf("Escolha:\n");

  scanf("%c", &escolha);

  switch (escolha) {
  case '1':
    printf("Raio:\n");
    scanf("%d", &num);
    area = 3.14 * num * num;
    printf("Area do circulo: ");
    printf("%.2f\n", area);
    break;

  case '2':
    printf("Lado:\n");
    scanf("%d", &num);
    area = num * num;
    printf("Area do quadrado: ");
    printf("%.2f\n", area);
    break;

  default:
    printf("Escolha Incorreta!\n");
  }
  return 0;
}