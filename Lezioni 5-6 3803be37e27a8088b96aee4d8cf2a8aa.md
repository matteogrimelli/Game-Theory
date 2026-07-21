# Lezioni 5-6

---

## Strategie Dominanti e Strategie Dominate

Una **strategia dominata** è una strategia che è sempre peggiore di un’altra, qualunque cosa facciano gli altri giocatori. Quindi un giocatore razionale non dovrebbe sceglierla

Una **strategia dominante**, invece, è una strategia che è sempre migliore delle altre, indipendentemente dalle scelte degli altri giocatori

Prisoner dilema :

marito e moglie ci sono 4 casi

- entrambi confessano prendono gli stessi anni 10,10
- entrambi mentono : prendono meno anni perchè convincono del falso 3,3
- uno dice il falso e laltro la verita : quello che dice la verita frega quello che dice il falso e quello che dice il falso prenderà molti anni e quello che dice il vero prendera pochi anni 1,25 / 25,1

Congresso e federale 

---

## Eliminazione strategia dominante

Algoritmo di **eliminazione successiva delle strategie dominate:**

1. Trovi una strategia dominata.
2. La elimini dal gioco.
3. Ricontrolli il gioco ridotto.
4. Ripeti finché non ci sono più strategie dominate.

L’idea è semplificare il gioco eliminando le scelte chiaramente irrazionali. Se alla fine rimane **un solo risultato possibile**, allora il gioco è detto **dominance solvable** e quel risultato è l’unico **equilibrio di Nash**

![image.png](image%2012.png)

---

## Gioco: Guessing Half Avarage

Ogni giocatore scrive un intero da 0 a 100, le carte verranno raccolte e verrà calcolata la media e il giocatore piu vicino a metà della media vince.

In questo gioco l’equilibrio di Nash è zero

Si usa l’**eliminazione iterata delle strategie dominate**:

1. La media non può mai superare **100**, quindi metà media non può superare **50**.
Quindi scegliere più di 50 non ha senso.
2. Se tutti capiscono questo, nessuno sceglierà più di **50**.
Allora la media massima diventa 50, e metà media massima diventa **25**.
3. Poi si elimina tutto ciò che è sopra 25.
4. Continuando così, si arriva progressivamente a **0**.

---

## P-beauty Contest

Il file spiega il **P-beauty contest**, un gioco simultaneo in cui ogni giocatore sceglie un numero tra **0 e 100**. Poi si calcola la **media** dei numeri scelti e vince chi si avvicina di più a: $p \cdot \text{media}$ dove p è un numero positivo, spesso p=2/3

Esempio:
se $p=\frac{2}{3}$ e media = 51 allora il numero obiettivo è $\frac{2}{3}\cdot 51 = 34$
Quindi vince chi ha scelto il numero piu vicino a 34

La parte importante è che l’**equilibrio di Nash** è che tutti scelgano 0
Perché se tutti scelgono 0, anche la media è 0 e quindi il target è 0. Nessun giocatore può migliorare scegliendo un numero diverso da solo.

L’intuizione è simile al gioco “Guessing Half Average”:

1. Se tutti possono scegliere massimo 100, il target massimo sarà minore di 100.
2. Quindi scegliere numeri troppo alti è irrazionale.
3. Sapendo questo, tutti abbassano le aspettative.
4. Il ragionamento si ripete fino ad arrivare a 0.

In sintesi: **con razionalità completa, tutti scelgono 0; nella pratica, però, le persone spesso scelgono numeri più alti perché non fanno tutti i passaggi logici fino in fondo**.

---

## Level k-model

Il level-k model è un modello che descrive giocatori con razionalita limitata. Non tutti ragionano fino all’equilibrio di nash, ma limitano i passaggi logici.

L’idea chiave è che dividere i giocatori in livelli

$L_0$: giocatore “base”, sceglie casualmente.

$L_1$: pensa che gli altri siano $L_0$

$L_k$: pensa che gli altri siano $L_{k-1}$

---

## Strategia Debolmente Dominanti

| Caso | Significato sintetico | Idea chiave |
| --- | --- | --- |
| **Strictly dominated** | Una strategia è **sempre peggiore** di un’altra, qualunque cosa facciano gli altri. | Va eliminata: non conviene mai. |
| **Weakly dominated** | Una strategia è **uguale o peggiore** di un’altra in tutti i casi, e **peggiore almeno in un caso**. | Si può eliminare, ma con attenzione: potresti perdere alcuni equilibri. |
| **Strictly dominant** | Una strategia è **sempre migliore** di tutte le altre, qualunque cosa facciano gli altri. | È la scelta razionale più forte. |
| **Weakly dominant** | Una strategia è **uguale o migliore** di tutte le altre in tutti i casi, e **migliore almeno in un caso**. | È una scelta razionale, ma non sempre dà un vantaggio netto. |

---

Steal or split 

gioco simultaneo dove due giochiatori possono decidere se fare split o steal di 13,600 euro casi :

- entrambi steal  : nessuno prende niente 0, 0
- entrambi split : si dividono il montepremi 50,50
- uno fa steal e l’altro split : quello che fa steal prende tutto il montepremi 100, 0

## Analisi best response

La **Best-Response Analysis**, cioè un metodo sistematico per trovare gli **equilibri di Nash** nei giochi in forma normale.

Una **best response** è la strategia migliore che un giocatore può scegliere, dato ciò che fa l’altro giocatore.

la strategia s_i è una risposta ottima se dà al giocatore i un payoff almeno uguale a qualsiasi altra strategia possibile, considerando fisse le strategie degli altri.

Un **equilibrio di Nash** può quindi essere definito così: ogni giocatore sta scegliendo una **best response** rispetto alle strategie degli altri.

| Passo | Cosa fai |
| --- | --- |
| 1 | Guardi le strategie di Column una per una. |
| 2 | Per ogni scelta di Column, trovi la risposta migliore di Row. |
| 3 | Poi fai il contrario: per ogni scelta di Row, trovi la risposta migliore di Column. |
| 4 | Cerchi le celle in cui entrambi stanno giocando una best response. |
| 5 | Quelle celle sono equilibri di Nash puri. |

La best-response analysis dipende solo dall’**ordine delle preferenze**, cioè dai **payoff ordinali**, non dai valori numerici precisi. Conta sapere quale risultato è preferito rispetto agli altri, non necessariamente quanto sia maggiore il payoff.

---