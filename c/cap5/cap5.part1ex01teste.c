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
#include <string.h>

int main() {
  char s[40];
  printf("digite algo:\n");
  fgets(s, 40, stdin);
  printf("saida: \"%s\" tamanho: %ld\n", s, strlen(s));
  s[strlen(s) - 1] = '\0'; // substituir \n por \0
  printf("saida: \"%s\" tamanho: %ld\n", s, strlen(s));
  return 0;
}