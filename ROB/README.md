# Notes
## PDF with exercise
https://szkopul.edu.pl/problemset/problem/p4hlBS7BwoH_rymSj2wtb5_J/site/?key=statement
## Z polskiego na nasze
### Robocik:
  * jest skierowany "do góry"
  * wykonuje komendy (d), aż do momentu w którym skończy się czas (t)
    * d -> o ile jednostek robot ma się przemieścić
    * komendy (d) są zapętlone - d1, d2, d3, d4, d1, d2, d3 ...
    * po każdej wykonanej komendzie (d) robocik obraca się o 90°
### Ruchy i czas:
  * Przejechanie jednej jednostki -> +1 sek (t)
  * Obrót o 90° -> +1 sek
### Input:
  1) Pierwsza wartość: n - ilość wszystkich komend; Druga wartość: t - czas (w sekundach)
  2) n wartości: d - komendy
  3) Pierwsza wartość: x; Druga wartość: y; - współrzędne miejsca dla którego liczymy ile razy zostało przekroczone
### Output:
  1) Ile razy punkt (x,y) został przekroczony