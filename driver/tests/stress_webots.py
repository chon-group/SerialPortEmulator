#!/usr/bin/python3

import unittest

import subprocess

import os

import os.path

import shutil


class TestStressWebots(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        print("setUpClass")
    
        self.__EmulatedPort = "/dev/ttyEmulatedPort"

        self.__Exogenous = "/dev/ttyExogenous"

        os.chdir("/tmp")

        while True:
            try:
                os.mkdir("stress_webots")
                subprocess.run( [ "touch" , "webots-cloned"  ] )
                break
            except FileExistsError:
                os.chdir("stress_webots")

                if os.path.isfile("webots-cloned") == False:

                    os.chdir("..")
            
                    shutil.rmtree(" stress_webots" )

                else:
                    break             

            except FileNotFoundError:
                pass

        # https://github.com/bptfreitas/FourWheels_With_ChonIDE_Webots

        # subprocess.run( [ "sudo" , "dmesg" , "-C" ] )

    def setUp(self):

        # Clearing the kernel log for the tests
        subprocess.run( [ "sudo" , "dmesg" , "-C" ] )

    def tearDown(self):

        filename = "exec{0}.log".format( 0 )

        with open(filename, "w") as output:

            ret = subprocess.run([ "sudo" , "dmesg" , "-T" ], 
                capture_output=True )

            output.write( ret.stdout.decode("utf-8") )

def suite():

    suite = unittest.TestSuite()
    # suite.addTest(TestSerialObject("test_01_VirtualBotSerialObjectInstantiated") )


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(suite())