import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# please do not sort hehe

st.image("./images/partners.png", use_column_width=True)

"""
# MigAI, czyli tłumaczenie języka migowego

[Repozytorium GitHub](https://github.com/jamnicki/mig-ai)


## Wprowadzenie
Osoby niesłyszące napotykają poważne wyzwania w codziennej komunikacji, zwłaszcza z osobami nieznającymi języka migowego. Brak tłumacza podczas kluczowych interakcji pogłębia tę przepaść, co podkreśla potrzebę innowacyjnych rozwiązań.  System tłumaczenia PJM może zrewolucjonizować interakcje osób niesłyszących, oferując im lepszy dostęp do informacji i eliminując bariery komunikacyjne, znacząco ułatwiając codzienne życie.
"""

st.image("./images/app_view.gif", use_column_width=True)


"""
## Dane
Dane wykorzystane do realizacji projektu pochodzą z dwóch źródeł. Pierwszym jest  Repozytorium Korpusu Polskiego Języka Migowego [2].  Jest to zbiór ponad 700 nagrań wypowiedzi migowych, które posiadają tłumaczenia w języku polskim. Ponadto zbiór został rozszerzony o dane z Korpusowego Słownika Polskiego Języka Migowego [1], które dostarczyły ponad 2000 nagrań przedstawiających użycie definicji w kontekście.

## Cel
Celem projektu było opracowanie efektywnego systemu tłumaczenia Polskiego Języka Migowego na tekst przy użyciu algorytmów sztucznej inteligencji.​
"""

"""
## Opis metody
Do rozwiązania problemu w pierwszej kolejności, wyekstrahowano z nagrań punkty kluczowe odpowiadające pozycjom elementów ciała przy użyciu modelu MediaPipe. Na podstawie tych punktów opracowane zostały dwa modele tłumaczące: Seq2Seq oraz Transformer [3,4].
"""
st.image("./images/metoda.png", use_column_width=True)


"""
## Ewaluacja
Na podstawie przeprowadzonych testów porównano jakość tłumaczeń dwóch modeli: Seq2Seq oraz Transformer, przy użyciu trzech metryk: BLEU, METEOR i TER. Dodatkowo wynik projektu był przedstawiony członkom Dolnośląskiego Oddziału Polskiego Związku Głuchych, gdzie uzyskano opinie oraz sugestie dotyczące opracowanego systemu. 
"""

"""
## Wyniki
Dla każdej z badanych architektur wyłoniono konfigurację parametrów, które osiągnęły najlepsze wyniki na zbiorze walidacyjnym. Model Transformer znacznie przewyższył rozwiązanie Seq2Seq, co wynika z jego zdolności do analizy i uczenia się złożonych zależności, charakterystycznych dla języka migowego i jego kontekstowej natury. Wykres poniżej przedstawia wyniki obu modeli na zbiorze testowym.
"""

st.image(
    "./images/hist.png",
    use_column_width=True,
    caption="BLEU mierzy pokrycie n-gramów tłumaczenia​ z wartością referencyjną​. METEOR, zmodyfikowana metryka BLEU​, uwzględniająca synonimy i strukturę zdaniową. TER określa liczbe edycji potrzebną do osiągnięcia​ poprawnego tłumaczenia",
)

st.image("./images/wyniki_tab.png", use_column_width=True)

"""
## Wnioski
Projekt MigAI z powodzeniem zademonstrował, że zaawansowane modele oparte na architekturze transformera skutecznie przekładają Polski Język Migowy, przewyższając tradycyjne metody. Projekt ten otwiera drogę do dalszych badań nad rozwojem bardziej zaawansowanych i precyzyjnych narzędzi tłumaczeniowych, które mogą znacząco wpłynąć na życie społeczności niesłyszących.


---

**Autorzy:** Iga Miller, Daria Kowal, Jędrzej Jamnicki,  Maciej Majewski

**Opiekun projektu:** prof. dr hab. inż. Urszula Markowska-Kaczmar

### Literatura

[1] Łacheta, J., Czajkowska-Kisil, M., Linde-Usiekniewicz, J., Rutkowski, P., Korpusowy słownik polskiego języka migowego   (Wydział Polonistyki Uniwersytetu Warszawskiego, Warszawa, 2016). Publikacja online

[2] Rutkowski, P., Łozińska, S., Filipczak, J., Łacheta, J., Mostowski, P., Jak powstaje korpus polskiego języka migowego (pjm)

[3] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., Polosukhin, I., Attention is all you need. 

[4] Sutskever, I., Vinyals, O., Le, Q.V., Sequence to sequence learning with neural networks, CoRR. 2014, tom abs/1409.3215.

[5] Lugaresi, C., Tang, J., Nash, H., McClanahan, C., Uboweja, E., Hays, M., Zhang, F., Chang, C., Yong, M.G., Lee, J., Chang, W., Hua, W., Georg, M., Grundmann, M., Mediapipe: A framework for building perception pipelines, CoRR. 2019

*Badania realizowane w ramach kursu “Projekt Naukowo-Wdrożeniowy” na kierunku Sztuczna Inteligencja w roku akademickim 23/24. Projekt realizowany przy współpracy z Pracownią Lingwistyki Migowej Uniwersytetu Warszawskiego.*

"""
