# Keyboard

This project is a 75% mechanical keyboard that I developed from scratch using KiCad. The idea was to create a compact, functional, and relatively simple keyboard, retaining the main keys of a conventional keyboard without taking up too much desk space.
The project was designed to be a real physical keyboard, so I didn't just focus on the visual aspect: I developed the circuit board (PCB), organized the key matrix, defined the electrical connections, and chose the necessary components so that the keyboard can be assembled and used later.

This project was going to be submitted to the Fabricate program, but I decided against it; I'll post it here instead. Because I thought halfway through, I have several other things to do, it's better not to. I didn't end up submitting it!

# Layout 
The keyboard uses a 75% layout, which retains virtually all the important functions of a full keyboard, but eliminates the spacebar and some less frequently used keys.
It has the main letter, number, and symbol keys, as well as keys such as the arrow keys, Shift, Ctrl, Alt, Enter, Backspace, and other function keys.

<img width="1010" height="368" alt="Screenshot_1" src="https://github.com/user-attachments/assets/b0c64295-bfcd-44dc-8839-41335232f39e" />
<img width="1444" height="572" alt="front_pcb" src="https://github.com/user-attachments/assets/3562a8d1-4a6e-404b-bcb3-3663f8fe4406" />


# PCB

The entire board was designed in KiCad. First, I arranged the keys according to the chosen layout and then started working on the electrical part.
The keys are part of a matrix of rows and columns. This way, it's not necessary to connect each key directly to a separate microcontroller pin. Each switch is connected to the matrix, allowing the microcontroller to identify which key was pressed.
I also added the components necessary for the correct reading of the matrix, including the diodes associated with the keys.

<img width="1388" height="540" alt="back_pcb" src="https://github.com/user-attachments/assets/fb5f11a6-8899-4c6a-8105-fc64ea92fd3f" />
<img width="1444" height="572" alt="front_pcb" src="https://github.com/user-attachments/assets/193cbaa0-e3ab-4c72-9146-9b73986189d9" />
<img width="1505" height="543" alt="pcb_editor" src="https://github.com/user-attachments/assets/68224921-2cd4-4391-ac17-4c523486000e" />

# Scheme
<img width="823" height="576" alt="general_scheme" src="https://github.com/user-attachments/assets/ed67c541-1166-4a61-8cd5-39cc680b5e78" />
<img width="801" height="368" alt="matrix" src="https://github.com/user-attachments/assets/418a0b90-6870-4562-aff9-e242011f00fb" />
<img width="394" height="658" alt="mx_stap" src="https://github.com/user-attachments/assets/c5f0386a-b822-470d-b5f7-da5ad212a7c6" />
<img width="847" height="721" alt="raspberrypi" src="https://github.com/user-attachments/assets/2c19bcc0-35dd-44c7-a84c-b253bd622d28" />


# Microcontroller
The keyboard has a microcontroller responsible for reading the key matrix and transforming the keystrokes into commands that the computer can interpret.
<img width="960" height="552" alt="image" src="https://github.com/user-attachments/assets/a6454b8a-7c1e-4d02-84c1-b22a872cb3e8" />


