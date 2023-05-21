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
int main(void) {
  char ch;
  int i;
  long int li;
  short s;
  unsigned int ui;
  float f;
  double d;
  long double ld;

  printf("Numero de bytes por tipo de dados:\n");
  printf("char:         %ld\n", sizeof(ch));
  printf("int:          %ld\n", sizeof(i));
  printf("long int:     %ld\n", sizeof(li));
  printf("short:        %ld\n", sizeof(s));
  printf("unsigned int: %ld\n", sizeof(ui));
  printf("float:        %ld\n", sizeof(f));
  printf("double:       %ld\n", sizeof(d));
  printf("long double:  %ld\n", sizeof(ld));
  return 0;
}