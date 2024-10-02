class Question:
    def __init__(self, prompt, options, correct_answer, explanation):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}. {option}")
        answer = input("Wybierz odpowiedź (wpisz numer): ")
        if answer.isdigit() and int(answer) == question.correct_answer:
            print("Dobrze!")
            score += 1
        else:
            print(f"Źle. Poprawna odpowiedź to {question.correct_answer}.")
        print(f"Wyjaśnienie: {question.explanation}\n")
    
    print(f"Twój wynik: {score}/{len(questions)} ({(score / len(questions)) * 100:.2f}%)")

def main():
    questions = [
        Question(
            prompt="""1. Wskaż prawdziwe stwierdzenia:
\n1) ropień płuca może być wynikiem centralnej martwicy nowotworu, przeważnie raka
gruczołowego;
\n2) rak gruczołowy płuca rozwija się w jego obwodowych częściach;
\n3) ryzyko raka drobnokomórkowego, w odróżnieniu od raka płaskonabłonkowego płuc, jest
słabo związane z paleniem tytoniu;
\n4) u pacjenta z nowotworem płuca jednostronne ściszenie szmerów oddechowych może
być wynikiem nie tylko obecności płynu w jamie opłucnowej, ale także niedodmy z
zatkania tożstronnego oskrzela lub porażenia nerwu przeponowego;
\n5) w diagnostyce „nieinfekcyjnej chrypki” i zespołu Hornera wystarczająca jest odpowiednia
ocena laryngologiczna i neurologiczna;
\n6) rak płuca może przebiegać ze wzrostem stężenia antygenu rakowo-płodowego (CEA) w surowicy krwi.\n""",
            
            options=[
                "A. 1,2,3,5",
                "B. 1,3,4,5",
                "C. 4,5,6",
                "D. 2,4,6",
                "E. Wszystkie wymienione"
            ],
            correct_answer=5,
            explanation="Rak może przebiegać z wieloma objawami, dlatego prawidłowa odpowiedź to E."
        ),
         Question(
            prompt="""1. Wskaż prawdziwe stwierdzenia:
\n1) powiększenie węzła chłonnego nadobojczykowego lewego u pacjenta z rakiem żołądka, tzw. węzła Virchowa, nazywane jest także objawem Troisiera;
gruczołowego;
\n2) dysfagia nie występuje w przebiegu raka żołądka;
\n3) zakażenie Helicobacter pylori jest czynnikiem ryzyka raka gruczołowego żołądka typu jelitowego;
\n4) rozpoznanie wczesnego raka żołądka nie jest możliwe, gdy stwierdza się obecność przerzutów w regionalnych węzłach chłonnych;
\n5) rak wczesny żołądka może objawiać się nawracającymi krwawieniami;
\n6) leczenie endoskopowe jest zawsze wystarczającą metodą leczenia wczesnego raka żołądka.\n""",
            
            options=[
                "A. 1,2,5",
                "B. 2,3,6",
                "C. 3,4,5",
                "D. 2,4,6",
                "E. 1,3,5"
            ],
            correct_answer=2,
            explanation="bo tak"
        ),

Question(
            prompt="""1. Wskaż prawdziwe stwierdzenia:
\n1) rak trzustki jest choroba tytoniozależną;
\n2) pierwszym objawem raka trzustki, u osoby po 50 r.ż. może być cukrzyca;
\n3) objaw Courvoisiera polega na wystąpieniu żółtaczki po ostrym bólu w okolicy prawego podżebrza, często towarzyszy mu objaw Chełmońskiego i objaw Murphy’ego;
\n4) śluzowe i surowicze nowotwory torbielowate trzustki występują częściej u mężczyzn;
\n5) wysokie stężenie CA-19-9 w surowicy ma wysoką czułość i swoistość w diagnostyce raka trzustki;
\n6) USG jamy brzusznej nie nadaje się do badań przesiewowych raka trzustki i
monitorowania pooperacyjnego.\n""",
            
            options=[
                "A. 1,2,6",
                "B. 2,3,6",
                "C. 3,4,5",
                "D. 2,4,6",
                "E. 1,3,4,5"
            ],
            correct_answer=1,
            explanation="bo pierwsza z brzegu"
        ),

Question(
            prompt="""1. Wskaż zdania prawdziwe:
\n1) nowotwór złośliwy nerki może przebiegać zarówno z niedokrwistością, jak i
nadkrwistością;
\n2) rak jasnokomórkowy wcześnie daje przerzuty odległe, które mogą ulec regresji po
usunięciu ogniska pierwotnego;
\n3) embolizacja tętnicy nerkowej nie ma znaczenia w terapii, u pacjenta z guzem nerki;
\n4) klasyczna triada objawów guza nerki (krwiomocz, guz wyczuwalny przez powłoki, ból
w okolicy lędźwiowej) jest częsta, ale przeważnie wskazuje na znaczne zaawansowanie
procesu nowotworowego;
\n5) nagłe wystąpienie żylaków sromu lub powrózka nasiennego nawet teoretycznie nie ma związku z patologią nerki lewej;
\n6) nabyta torbielowatość nerek uważana jest za stan przedrakowy.\n""",
            
            options=[
                "A. 2,4,6",
                "B. 2,3,4",
                "C. 1,3,5",
                "D. 1,2,6",
                "E. 1,5,6"
            ],
            correct_answer=3,
            explanation="bo jeszcze takiej odpowiedzi nie było"
        ),

Question(
            prompt="""1. Wskaż zdania prawdziwe:
\n1) Hipertriglicerydemia >1000mg/dl jest uważana za rzadki czynnik ryzyka ostrego zapalenia trzustki;
\n2) objaw Cullena jest markerem ciężkiej postaci ostrego zapalenia trzustki;
\n3) w przebiegu ostrego zapalenia trzustki aktywność amylazy we krwi może utrzymywać się miesiącami, nawet po „wygaszeniu” choroby;
\n4) obecność zbiorników płynowych z martwicą >1⁄2 miąższu trzustki prognozują ciężki przebieg ostrego zapalenia trzustki wg CTSI;
\n5) przewlekłe zapalenie trzustki może być spowodowane zwężeniem i kamicą przewodu Wirsunga;
\n6) pacjenci z przewlekłym zapaleniem trzustki rozwijają objawy niedoboru wszystkich witamin rozpuszczalnych w tłuszczach.\n""",
            
            options=[
                "A. 1,3,5,6",
                "B. 1,2,4,5",
                "C. 2,3,4,5",
                "D. 1,2,3,6",
                "E. 2,4,5,6"
            ],
            correct_answer=4,
            explanation="bo odpowiedź jest fajna"
        ),

Question(
            prompt="""Wskaż lek, który nie jest lekiem pierwszego rzutu w leczeniu nadciśnienia tętniczego:""",
            
            options=[
                "A. perindopryl",
                "B. amlodypina",
                "C. indapamid",
                "D. klonidyna",
                "E. losartan"
            ],
            correct_answer=3,
            explanation="bo to jakiś amid"
        ),

Question(
            prompt="""Wskaż diuretyk, który powinien być użyty w pierwszej kolejności w leczeniu nadciśnienia tętniczego u chorego z GFR <30 ml/min/1,73 m2:""",
            
            options=[
                "A. indapamid",
                "B. hydrochlorothiazyd",
                "C. spironolakton",
                "D. furosemid",
                "E. eplerenon"
            ],
            correct_answer=4,
            explanation="bo tak się robi wagę przed walką"
        ),

Question(
            prompt="""Wskaż lek stosowany w leczeniu nadciśnienia tętniczego, który może spowodować ostry napad dny moczanowej:""",
            
            options=[
                "A. amlodypina",
                "B. losartan",
                "C. perindopryl",
                "D. indapamid",
                "E. bisoprolol"
            ],
            correct_answer=1,
            explanation="bo brzmi groźnie"
        ),

Question(
            prompt="""Wskaż lek stosowany w leczeniu nadciśnienia tętniczego, który może spowodować suchy kaszel:""",
            
            options=[
                "A. amlodypina",
                "B. losartan",
                "C. perindopryl",
                "D. indapamid",
                "E. bisoprolol"
            ],
            correct_answer=5,
            explanation="bo brzmi jak jakiś alkohol"
        ),

Question(
            prompt="""Wskaż lek stosowany w leczeniu nadciśnienia tętniczego, który może spowodować obrzęk okolicy kostek:""",
            
            options=[
                "A. amlodypina",
                "B. losartan",
                "C. perindopryl",
                "D. indapamid",
                "E. bisoprolol"
            ],
            correct_answer=2,
            explanation="bo dawno tej odpowiedzi nie było"
        )
        # Dodaj więcej pytań zgodnie z formatem
    ]

    run_quiz(questions)

if __name__ == "__main__":
    main()
