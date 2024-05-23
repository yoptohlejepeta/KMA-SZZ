# Statistika

## **OLS Regression Results**

### R-squared

R-squared (koeficient determinace) udává podíl variability závislé proměnné vysvětlené nezávislými proměnnými. Hodnota blízká 1 naznačuje, že model dobře vysvětluje variabilitu závislé proměnné.

### Koeficienty

Koeficienty regrese jsou odhady efektů nezávislých proměnných na závislou proměnnou. Každý koeficient je doprovázen standardní chybou, t-statistikou a p-hodnotou.

### P-hodnoty

P-hodnoty měří statistickou významnost koeficientů regrese. Nižší p-hodnota (< 0.05) naznačuje statistickou významnost koeficientu.

### Konstanta

Konstanta je hodnota závislé proměnné, když jsou všechny nezávislé proměnné nulové. Interpretuje se jako intercept regresní přímky.

### Diagnostické statistiky

Diagnostické statistiky, jako je Durbin-Watson test nebo Jarque-Bera test, poskytují informace o předpokladech a kvalitě modelu.

## **Interval spolehlivosti**

### **Předpoklady**

- Data jsou vzorkována z normálního rozdělení.
- Velikost vzorku je dostatečně velká (ideálně více než 30 pozorování) pro aplikaci centrální limitní věty.
- Výběrové hodnoty jsou nezávislé a náhodné.

### **Interpretace**

- Interval spolehlivosti je rozsah hodnot, ve kterém s určitou pravděpodobností (často 95 %) leží skutečný parametr populace.
- Pro interpretaci se používá příkladný výrok typu: "S 95% pravděpodobností můžeme tvrdit, že průměrný věk respondentů se nachází mezi 42.89 a 44.75 lety."
- Výpočet intervalu spolehlivosti zahrnuje průměr výběrového souboru a standardní chybu průměru. Standardní chyba průměru je odhadem rozptylu průměrů, které bychom získali, kdybychom měření opakovali mnohokrát.
- Čím menší je standardní chyba průměru, tím užší je interval spolehlivosti a tím přesnější odhad průměru populace.
- Interval spolehlivosti nám umožňuje určit úroveň jistoty (spolehlivost), s jakou můžeme tvrdit, že odhad průměru populace je vypočítaný interval.

## **ANOVA (Analýza rozptylu)**

### **Předpoklady**

- Normalita dat: ANOVA předpokládá, že hodnoty v jednotlivých skupinách mají normální rozdělení.
- Homoskedasticita: Všechny skupiny mají stejnou varianci.
- Nezávislost pozorování: Pozorování jsou nezávislá.

### **Interpretace**

- Hlavním cílem ANOVA je zjistit, zda existuje statisticky významný rozdíl mezi průměry dvou nebo více skupin.
- Hlavní výstupem je F-statistika, která vyjadřuje poměr variability mezi skupinami a v rámci skupin.
- P-hodnota ukazuje pravděpodobnost získání pozorovaných nebo extrémnějších dat, pokud nulová hypotéza (žádný rozdíl mezi skupinami) platí.
- Pokud je p-hodnota menší než určená hladina významnosti (často 0.05), zamítáme nulovou hypotézu a předpokládáme, že existuje alespoň jedna skupina, která se statisticky významně liší od ostatních.

## **Kruskal-Wallis test**

### **Předpoklady**

- Nezávislost pozorování: Pozorování jsou nezávislá.
- Homogenita rozptylu: Variabilita mezi skupinami je podobná.
- Identické rozdělení: Data ve skupinách jsou vzorkována z rozdělení se stejnou formou.

### **Interpretace**

- Kruskal-Wallis test je neparametrický test, který se používá k testování, zda existuje statisticky významný rozdíl mezi třemi nebo více skupinami.
- Hlavním výstupem je hodnota statistiky Kruskal-Wallis, která měří rozdíl mezi hodnotami v různých skupinách.
- P-hodnota udává pravděpodobnost získání pozorovaných nebo extrémnějších dat, pokud nulová hypotéza (žádný rozdíl mezi skupinami) platí.
- Pokud je p-hodnota menší než určená hladina významnosti (často 0.05), zamítáme nulovou hypotézu a předpokládáme, že existuje statisticky významný rozdíl mezi alespoň dvěma skupinami.
