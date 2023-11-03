# Robocik_zadanie_rekrutacyjne

Stworzona przezemnie paczka znajduje się w /zadanie/src/ i nazywa się plansza_pionek

Stowrzone przezmnie noedy znaduja sie w /zadanie/src/plansza_pionek/plansza_pionek i są to plansza_i_pionek.py przechowywujaca
dane o planszy oraz pionku, oraz ruch.py pobierajacy dane z klawiatury i wysylajacy polecenia na topic o nazwie ,,topic"

Jakby jakimś cudem colcon zbudowany jest w folderze /zadanie/ nie działał, to nalezy wpisac w jego lokalizacji colcon build

Aby ros2 run zadzialal, trzeba w gedit /.bashrc dodac source (lokalizacja pliku /Robocik_zadanie_rekrutacyjne_mainzadanie/install/setup.bash) 
u mnie to source ~/Robocik_zadanie_rekrutacyjne_main/zadanie/install/setup.bash oraz w workspace ,,zadanie" trzeba wpisac komende source ~/.bashrc
probowalem to obec tak, aby nie trzeba bylo tego wpisywac, ale nie udalo mi sie :c 

Aby odpalic node z plansza nalezy wpisac 
ros2 run plansza_pionek plansza_pionek
Po uruchomieniu w tym samym terminalu odpali się plansza( nie zdazylem
nauczyc sie jak to robic w pygame, aby otwieralo sie w okienku oddzielnym )

Aby odpalic node z poruszaniem sie nalezy wpisac
ros2 run plansza_pionek ruch
Po uruchomieniu w tym samym terminalu odpali sie program wczytujacy wcisniete klawisze
(nie trzeba zatwierdzac ich enterem). Mozna sterowac WSADem albo strzalkami - dzialaja oba


Info na temat  tego co dzieje się w node-ach jest opisane w ich kodach źródłowych
W razie wątpliwosci mozecie się ze mna kontaktowac na maila na jaki wyslalem wam tez link do githuba 
