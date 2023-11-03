#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import os
import readchar

class Mynode( Node ):

    def __init__( self ):

        super().__init__( "ruch" )
        self.get_logger().info( "dziala" )
        
        self.pub = self.create_publisher( Twist , "topic" , 2 )         #publisher
        self.timer_ = self.create_timer( 0.5 , self.send_command )      #timer, ktory po otrzymaniu danych wysyla je na topic


    def send_command( self ):       #metoda wysylajaca dane o zmianie polozenia pionka jako x,y

        msg = Twist()               #nie znam innego typu, dzieki ktoremu mozna wysylac wiecej niz jedna dane
        msg.linear.x = 0.0
        msg.linear.y = 0.0

        os.system( 'clear' )
        print("Sterowanie: WSAD lub strzałki")
        a = readchar.readkey()      #wychwytuje i pobiera klawisz, ktory zostal wcisniety

        match a:       #funkcja warunkowa

            case 'w' | "\x1b\x5b\x41":  #
                msg.linear.x = -1.0     #
                                        # gdy wcisniemy WSAD lub strzałki
            case 's' | "\x1b\x5b\x42":  # (te nazwy po znaku logicznym "|")
                msg.linear.x = 1.0      # to zmieniaja sie wspolzedne
                                        # wysylane na topic
            case 'a' | "\x1b\x5b\x44":  #
                msg.linear.y = -1.0     #
                                        #
            case 'd' | "\x1b\x5b\x43":  #
                msg.linear.y = 1.0      #

        self.pub.publish(msg)       #publikowanie na topic danych



def main( args = None ):
    rclpy.init( args = args )
    node = Mynode()
    rclpy.spin( node )
    rclpy.shutdown()

if __name__ == '__main__':
    main()