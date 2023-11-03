#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import os
from colorama import Back


class Mynode( Node ):

    def __init__( self ):

        super().__init__( "plansza_i_pionek" )
        self.get_logger().info( "dziala" )

        self.plansza = Plansza()    #stworzenie obiektu plansza
        self.pionek = Pionek()      # i obiektu pionek

        self.sub = self.create_subscription( Twist , "topic" , self.get_command , 10)   #subscriber

        self.timer_ = self.create_timer( 0.2 , self.wypisywanie )       #timer, ktory dynamicznie wyswietla plansze oraz pobiera dane z topicu


    def get_command( self , msg: Twist ):

        self.pionek.ruch( int(msg.linear.x) , int(msg.linear.y) )
        #po przechwyceniu danych nastepuje ich wyslanie do metody klasy Pionek

    def wypisywanie( self ):

        os.system( 'clear' )    
        self.plansza.write( self.pionek.x , self.pionek.y )  #wypisywanie planszy dzieki metodzie klasy Plansza
        


class Plansza():

    def __init__( self ):

        self.m = 20         #nadanie wielkosci
        self.n = 15         #Planszy jako n x m
        self.tablica =[ [" "] * self.m ] * self.n   #storzenie tablicy dwuwymiarowej
    

    def write( self , x , y ):  #metoda wypisujaca

        print()         #dla lepszej widocznosci
        print()         #obnizenie planszy

        for i in range( len(self.tablica) ):    #petla przechodzaca przez wiersze

            print( "   ", end = '' )            #dla lepszej widocznosci  przesuniecie planszy
            print( Back.CYAN , end = '' )       #start zapisywania planszy

            for j in range( len(self.tablica[i]) ):     #petla przechodzaca przez kolumny
            
                if( i == x and j == y ):                                    #jezeli pionek znaduje sie na danym polu
                    print( Back.BLUE + self.tablica[i][j] , end=' ' )       #to zmiana koloru pola reprezentujaca polozenie pionka
                    print( Back.CYAN , end='' )                             #zmiana koloru pola na kolor planszy

                else:
                    print( self.tablica[i][j] , end=' ' )   #jezeli nie ( na polu nie ma pionka ) to zapisuje dalej plansze

            print( Back.RESET )                 #koniec zapisywania planszy


class Pionek():

    def __init__( self ):
        self.x = 5          #poczatkowe wspolzedne
        self.y = 5          #polozenia pionka


    def ruch( self ,linear_x , linear_y ):  #metoda zmieniajaca polozenia
        wielkosc_mapy_y = Plansza().m   #
        wielkosc_mapy_x = Plansza().n   #wielkosc planszy

        if( self.x + linear_x < wielkosc_mapy_x and self.x + linear_x >= 0 ):   #
            self.x += linear_x                                                  #jezeli pionek po poruszeniu znajdowalby sie w planszy
                                                                                #to nastepuje zmiana wspolzednej polozenia pionka o
        if( self.y + linear_y < wielkosc_mapy_y and self.y + linear_y >= 0 ):   #dane pobrane z topicu
            self.y += linear_y                                                  #
        

def main( args = None ):
    rclpy.init( args = args )
    node = Mynode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()