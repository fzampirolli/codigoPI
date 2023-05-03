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
#include <stdlib.h>  // malloc e free

int* leiaVetor(int n) {
  int* v = malloc(n * sizeof(int));
  for (int i = 0; i < n; i++) {
    scanf("%d", &v[i]);
  }
  return v;
}

void escrevaVetor(int* v, int n) {
  for (int i = 0; i < n; i++) {
    printf("%d\n", v[i]);
  }
}

int main(void) {
  // ENTRADA DE DADOS
  int n, * v1;   // variaveis de referência v1
  printf("Digite o tamanho do vetor: ");
  scanf("%d", &n);
  int* v2 = malloc(100 * sizeof(int));
  printf("Digite os elementos: ");
  v1 = leiaVetor(n);
  // PROCESSAMENTO
  for (int i = 0; i < n; i++) {
    int max = v1[i];
    if (i - 1 >= 0 && max < v1[i - 1])
      max = v1[i - 1];
    if (i + 1 < n && max < v1[i + 1])
      max = v1[i + 1];
    v2[i] = max;
  }
  // SAÍDA:
  printf("\nv2:\n");
  escrevaVetor(v2, n);
  free(v1); // liberar memória alocado com malloc
  free(v2);
  return 0;
}