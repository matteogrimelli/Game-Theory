# Lezioni 9-10

---

## Giochi Two-Stage

I **Two-Stage Games sono** giochi che combinano **mosse simultanee** e **mosse sequenziali**. L’idea è che alcune situazioni strategiche non sono solo simultanee o solo sequenziali, ma hanno più fasi

Un two-stage game ha due fasi:

- Prima fase: i giocatori fanno una scelta iniziale, spesso simultanea.
- Seconda fase: in base a ciò che è successo nella prima fase, si gioca un altro sotto-gioco, che può essere sequenziale o simultaneo.

Un **two-stage game** si risolve così:

1. risolvi prima i sotto-giochi della seconda fase;
2. sostituisci i payoff ottenuti nella prima fase;
3. risolvi il gioco iniziale con best-response analysis o rollback.

---

## Information sets, subgames

Un information set è un insieme di nodi che un giocatore non riesce a distinguere quando deve scegliere. Quindi deve scegliere la stessa azione in tutti quei nodi.

Un gioco ha informazione perfetta se ogni giocatore sa sempre esattamente in quale nodo si trova. Quindi tutti gli information set contengono un solo nodo.
Un gioco ha informazione imperfetta se almeno un information set contiene più nodi

<aside>
⚠️

**Subgames e Information Set**: un sottogioco può iniziare da un nodo solo se non “taglia” un information set. Cioè, non puoi iniziare un sottogioco da un nodo se poi dentro quel ramo c’è un information set collegato anche a nodi esterni.

</aside>

| Concetto | Significato |
| --- | --- |
| **Perfect recall** | Il giocatore ricorda le sue decisioni passate |
| **Imperfect recall** | Il giocatore può “dimenticare” una propria scelta precedente |

---

## Equilibrio subgame-perfect (SPE)

In un gioco sequenziale, una strategia non è solo una singola azione, ma un **piano completo di azione**: il giocatore deve specificare cosa fare in ogni possibile situazione del gioco, anche in quelle che magari non si verificheranno mai.

Esempio: se **Congress** muove per primo, ha solo 2 strategie:
$\text{Balance}, \quad \text{Deficit}$

La **FED**, invece, muove dopo e può trovarsi in due casi diversi: dopo **Balance** o dopo **Deficit**. Quindi deve specificare cosa fare in entrambi i casi. Per questo ha 4 strategie:

$$
(\text{Low if Balance, High if Deficit})\\
(\text{High if Balance, Low if Deficit})\\
(\text{Low always})\\
(\text{High always})
$$

Il punto importante è che, se rappresentiamo il gioco sequenziale in forma strategica, possiamo trovare più **equilibri di Nash**. Però alcuni di questi non sono credibili dal punto di vista sequenziale.

La differenza è questa:

| Concetto | Significato |
| --- | --- |
| **Nash Equilibrium** | Nessuno vuole deviare dalla propria strategia, date le strategie degli altri |
| **Rollback / SPE** | Ogni scelta deve essere ottimale in ogni sottogioco, anche fuori dal percorso di equilibrio |

Esempio: una strategia come **“High always”** può far parte di un equilibrio di Nash, ma non essere credibile, perché in alcuni sottogiochi la FED, se davvero arrivasse lì, preferirebbe scegliere **Low**. Quindi quella strategia non è ottimale in ogni possibile punto del gioco

<aside>
⚠️

Qui nasce lo **SPE**: un equilibrio è **subgame perfect** se le strategie formano un equilibrio non solo nel gioco intero, ma anche in ogni sottogioco. $\text{SPE} \subseteq \text{Nash Equilibrium}$

</aside>

In sintesi: **l’equilibrio di Nash può includere minacce non credibili; lo SPE elimina queste minacce richiedendo che ogni decisione sia razionale in ogni possibile sottogioco.** Nei giochi finiti con informazione perfetta, lo SPE si trova con la **rollback induction**.

---

## Equilibrio subgame-perfect (giocatori multipli)

Differenza tra **equilibri di Nash** e **Subgame Perfect Equilibrium** usando il gioco del **giardino a 3 giocatori:**

Nel gioco originale i giocatori scelgono **in sequenza** se contribuire o no al giardino. Con il metodo del **rollback**, si trova un unico equilibrio coerente con il ragionamento all’indietro

Modificando il gioco rendendolo **simultaneo**: tutti scelgono senza osservare prima le scelte degli altri. In questo caso compaiono **4 equilibri di Nash**: (due contribuiscono,uno no) e anche (nessuno contribuisce)

Quindi passando da gioco sequenziale a simultaneo si perde il **vantaggio del primo giocatore** e compaiono più equilibri

La parte centrale mostra poi che anche un gioco sequenziale può essere rappresentato in **forma strategica**, cioè come matrice di strategie complete. 

Questo perché una strategia in un gioco sequenziale è un **piano completo di azione**, cioè deve specificare cosa fare in ogni possibile nodo decisionale.

Analizzando il gioco in forma strategica si trovano molti equilibri di Nash, Però non tutti sono credibili. Alcuni prevedono azioni irrazionali in parti del gioco che magari non vengono raggiunte.

Qui entra il concetto di **Subgame Perfect Equilibrium**: un equilibrio è subgame perfect solo se le strategie sono ottimali **in ogni sottogioco**, non solo lungo il percorso effettivamente giocato.
Formula: $\text{SPE} \subseteq \text{NE}$ → Cioè: ogni SPE è anche un equilibrio di Nash, ma non ogni equilibrio di Nash è subgame perfect.

In sintesi: l’equilibrio di Nash richiede razionalità globale; lo SPE richiede razionalità credibile in ogni parte del gioco, anche fuori dal percorso principale.

---

## Giochi sequenziali con informazione imperfetta (ed equilibri puri)

Nei giochi con **informazione perfetta**, tutti gli information set sono singoli nodi, quindi si può usare direttamente la **backward induction**. 
Nei giochi con **informazione imperfetta**, invece, prima bisogna individuare i **subgames validi**, cioè sottogiochi che **non tagliano information sets**. Se un information set collega nodi dentro e fuori dal sottogioco, allora quel sottogioco non è valido.

Per trovare uno **SPE** con informazione imperfetta si usa una versione estesa della backward induction:

1. Trova un sottogioco valido che non contiene altri sottogiochi.
2. Risolvi quel sottogioco cercando un **equilibrio di Nash**.
3. Sostituisci il sottogioco con un nodo terminale che ha i payoff dell’equilibrio trovato.
4. Ripeti finché rimane solo il gioco iniziale.

$\text{SPE} = \text{NE in ogni sottogioco}$

<aside>
⚠️

Punto importante: Se un sottogioco ha **più equilibri di Nash**, ognuno può generare uno **SPE diverso** nel gioco originale. Quindi, per trovare tutti gli SPE, bisogna considerare i possibili equilibri nei sottogiochi.

</aside>

In sintesi: **con informazione perfetta usi direttamente backward induction; con information sets devi prima risolvere i sottogiochi come giochi strategici, poi sostituirli con i payoff di equilibrio e risalire l’albero.**

---

## Extra: Gambit

Gambit è un software per modellare e analizzare giochi in teoria dei giochi. Serve soprattutto per costruire giochi in **forma estesa** o **forma strategica** e calcolare gli equilibri

| Funzione | Significato |
| --- | --- |
| Creare giochi in forma estesa | Alberi di gioco con mosse sequenziali |
| Creare giochi in forma strategica | Tabelle/matrici dei payoff |
| Aggiungere giocatori | Di default ce ne sono 2, ma se ne possono aggiungere altri |
| Aggiungere mosse | Click destro sui nodi per inserire azioni |
| Aggiungere chance moves | Mosse casuali con probabilità |
| Creare information sets | Per rappresentare informazione imperfetta |
| Inserire payoff | Cliccando sui nodi terminali |
| Calcolare equilibri | Dal menu **Tools → Compute equilibria** |

Forma estesa: Per creare un gioco ad albero:

1. aggiungi le mosse ai nodi;
2. scegli il numero di azioni disponibili;
3. rinomina le azioni cliccando sulle etichette;
4. aggiungi eventuali nodi di chance;
5. aggiungi eventuali information sets;
6. inserisci i payoff nei nodi terminali.

> In Gambit si possono creare collegando nodi decisionali nello stesso insieme informativo.
> 

Gambit può calcolare gli **equilibri di Nash** usando: Tools → Compute equilibria

<aside>
⚠️

La GUI di Gambit **non mostra direttamente solo gli SPE**, ma calcola equilibri sulla **forma strategica** del gioco. Quindi, nei giochi sequenziali, alcuni equilibri trovati potrebbero non essere **subgame perfect**.

</aside>

Strategie miste: Quando Gambit mostra una strategia con probabilità, significa che il giocatore sceglie quella strategia con una certa probabilità. $P(\text{Confess}) = 1, \quad P(\text{Deny}) = 0$

---