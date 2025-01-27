# SerialPortEmulator

This is a serial port emulator. This is done by creating pairs of ports on /dev where writing data on one port can be read on the pair and vice-versa.


## Installation

1) Install the dependencies. On your Debian-like Linux machine, run:

```
sudo apt install python3-serial linux-headers-`uname -r` gcc binutils make
```

2) Inside the driver folder, run:

```
make clean all
sudo make modules_install
sudo make install
```

3) Set read and write permissions on the pairs of devices to be used

Example: for the EmulatedPort 0 device:

```
sudo chmod 777 /dev/ttyEmulatedPort0
sudo chmod 777 /dev/ttyExogenous0
```

## Uninstallation

Inside the 'driver' folder, run: 

```
sudo make uninstall
```

## Use 

After the installation, by default, it will be instatiated on /dev many pairs of devices:

- /dev/ttyEmulatedPort0 <---> /dev/ttyExogenous0
- /dev/ttyEmulatedPort1 <---> /dev/ttyExogenous1
...

And so on. Writing on one device will make its content to be read on the other pair, and vice-versa

You MUST at least execute a read operation on the Exogenous port to make the OS create the necessary structures

## Example
In a terminal window, execute the command below to put the emulated port waiting for incoming data

Open another terminal window and run the below command. On the first terminal Window. It should appear the message.

![Screenshot_20240117_201825](https://github.com/chon-group/dpkg-virtualport-driver/assets/32855001/3aefe904-f3cd-49a9-a6e8-91eeb423b245)

## Copyright
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />ChonIDE is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The licensor cannot revoke these freedoms as long as you follow the license terms:

* __Attribution__ — You must give __appropriate credit__ like below:

FREITAS, Bruno Policarpo Toledo; LAZARIN, Nilson Mori; PANTOJA, Carlos Eduardo. Uma Proposta de Emulador de Portas Seriais para Sistemas Multiagentes Embarcados. _In_: Workshop-Escola de Sistemas de Agentes, seus Ambientes e Aplicações (WESAAC), 17. , 2023, Pelotas/RS. Anais [...]. Pelotas: UFPel, 2023 . p. 55-66. URL: [https://zenodo.org/record/8329081](https://www.researchgate.net/publication/373484449_Uma_Proposta_de_Emulador_de_Portas_Seriais_para_Sistemas_Multiagentes_Embarcados)

### Bibtex

```
@inproceedings{freitas2023,
 author = {Freitas, Bruno Policarpo Toledo and Lazarin, Nilson Mori and Pantoja, Carlos Eduardo},
 title = {Uma {Proposta} de {Emulador} de {Portas} {Seriais} para {Sistemas} {Multiagentes} {Embarcados}},
 booktitle = {Anais do XVII Workshop-Escola de Sistemas de Agentes, seus Ambientes e Aplicações (WESAAC 2023)},
 location = {Pelotas/RS},
 year = {2023},
 pages = {55--66},
 publisher = {UFPel},
 address = {Pelotas, RS, Brasil},
 url = {https://zenodo.org/record/8329081}
}
