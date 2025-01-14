#!/usr/bin/python3

import unittest

import subprocess

import os

import os.path

import shutil


class TestStressWebots(unittest.TestCase):

    i = 0

    @classmethod
    def setUpClass(self):

        i = 1

        print("setUpClass")
    
        self.__EmulatedPort = "/dev/ttyEmulatedPort"

        self.__Exogenous = "/dev/ttyExogenous"

        os.chdir("/tmp")

        while True:
            try:                
                os.mkdir("stress_webots")

                os.chdir("stress_webots")

                with open("webots-cloned", "w") as f:
                    pass                

                break

            except FileExistsError:
                os.chdir("stress_webots")

                if os.path.isfile("webots-cloned") == False:

                    os.chdir("..")
            
                    shutil.rmtree( "stress_webots" )

                else:
                    break             

            except FileNotFoundError:
                pass

        repo = "https://github.com/bptfreitas/FourWheels_With_ChonIDE_Webots"
        
        subprocess.run( [ "git" , "clone" , repo ] )

        os.chdir( "FourWheels_With_ChonIDE_Webots" )

        os.chdir( "controllers/four_wheels_collision_avoidance" )

        repo = "https://github.com/bptfreitas/JavinoCLibrary.git"

        subprocess.run( [ "git" , "clone" , repo ] )

        os.chdir( "JavinoCLibrary" )

        subprocess.run( [ "make" , "clean", "all"] )

        os.chdir( ".." )

        my_env = os.environ.copy()

        my_env["WEBOTS_HOME"] = "/usr/local/webots"

        subprocess.run( [ "make", "clean" ] , \
            env= my_env )

        subprocess.run( [ "make", "all" ] , \
            env= my_env )            
    
    def setUp(self):

        # Clearing the kernel log for the tests
        subprocess.run( [ "sudo" , "dmesg" , "-C" ] )

    def tearDown(self):

        test_name = self.id().split(".") [ 2 ]

        filename = "stress_webots-{0}.log".format( test_name )

        with open(filename, "w") as output:

            ret = subprocess.run([ "sudo" , "dmesg" , "-T" ], 
                capture_output=True )

            output.write( ret.stdout.decode("utf-8") )

    def test_stress_main(self):

        os.chdir( "../.." )

        subprocess.run( [ "webots" , "worlds/4_wheels_robot.wbt" ] )

        self.assertEqual( True, True )

def suite():

    suite = unittest.TestSuite()
    suite.addTest( TestStressWebots("test_stress_main") )

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run( suite() )