# Algorytm-Dijkstry
Algorytm ten służy do znajdowania najkrótszych ścieżek od wierzchołka źródłowego do wszystkich innych wierzchołków w grafie ważonym.

Główna funkcja w tej implementacji to **dijkstra(G, w, s)**. Przyjmuje ona trzy parametry:

**G**: Słownik reprezentujący graf, gdzie klucze to wierzchołki, a wartości to listy sąsiednich wierzchołków.
**w**: Słownik reprezentujący wagi krawędzi, gdzie klucze to krotki **(u, v)** reprezentujące krawędź między wierzchołkami **u** i **v**, a wartości to odpowiadające im wagi.
**s**: Wierzchołek źródłowy, od którego mają być znalezione najkrótsze ścieżki.
Algorytm działa w następujący sposób:

1)Inicjalizuje słowniki **odleglosc** i **poprzednik**, które przechowują najkrótsze odległości od wierzchołka źródłowego **s** oraz poprzednie wierzchołki na najkrótszych ścieżkach dla każdego wierzchołka w grafie.

2)Odległość do wszystkich wierzchołków jest ustawiana na nieskończoność, z wyjątkiem wierzchołka źródłowego **s**, którego odległość wynosi 0.

3)Tworzony jest zbiór **Q** zawierający wszystkie wierzchołki w grafie.

4)Dopóki **Q** nie jest pusty, wybierany jest wierzchołek **u** o najmniejszej odległości.

5)Dla każdego sąsiedniego wierzchołka **v** wierzchołka **u**, obliczana jest nowa odległość poprzez dodanie wagi krawędzi między **u** i **v** do odległości **u**. Jeśli nowa odległość jest mniejsza od obecnej odległości do **v**, odległość ta zostaje zaktualizowana, a **u** staje się poprzednikiem **v**.

6)Proces kontynuowany jest, dopóki wszystkie wierzchołki nie zostaną odwiedzone.

7)Algorytm zwraca słownik **odleglosc**, który zawiera najkrótsze odległości od wierzchołka źródłowego **s** do wszystkich innych wierzchołków, oraz słownik **poprzednik**, który zawiera poprzedników na najkrótszych ścieżkach.


W przykładzie podanym w kodzie, algorytm jest zastosowany do grafu **G** z odpowiadającymi mu wagami krawędzi **w**, rozpoczynając od wierzchołka źródłowego '**A**'. Wyświetlane są najkrótsze odległości i poprzednicy na ścieżkach.

![d1](https://github.com/maxyymmm/Algorytm-Dijkstry/assets/120425774/9dc8671b-0950-46aa-9acb-bd5501597e89)

![d2](https://github.com/maxyymmm/Algorytm-Dijkstry/assets/120425774/ed166e74-2076-484a-b56d-f083e49d5958)

