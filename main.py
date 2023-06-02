import os,datetime,time
from qiskit import QuantumCircuit, Aer, execute
import numpy as np


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    print("Menu:")
    print("A)  Play Guess the Quantum State game")
    print("B)  Play Quantum Coin Flip game")
    print("X)  Exit")

def generate_random_state():
    # Create a quantum circuit with 1 qubit
    circuit = QuantumCircuit(1)

    # Generate random angles for the state vector
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2*np.pi)

    # Apply the rotation gates to create the random state
    circuit.rx(theta, 0)
    circuit.rz(phi, 0)

    # Simulate the circuit using the local Aer simulator
    simulator = Aer.get_backend('statevector_simulator')
    job = execute(circuit, simulator)

    # Get the resulting state vector
    result = job.result()
    statevector = result.get_statevector(circuit)

    # Return the random state vector
    return statevector

def value_error():
    while True:
        try:
            theta_guess = float(input("Enter your guess for theta: "))
            phi_guess = float(input("Enter your guess for phi: "))
            return theta_guess, phi_guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def guess_quantum_state():
    # Generate a random quantum state
    target_state = generate_random_state()

    print("Guess the Quantum State Game")
    print("-----------------------------")
    print("I have generated a random quantum state. Your task is to guess it.")
    print("The state can be represented as a superposition of |0⟩ and |1⟩.")
    print("You need to guess the rotation angles theta and phi that create the state.")
    print("The angles are in radians and range from 0 to 2π.")
    print("Let's begin!")

    while True:
        theta_guess,phi_guess=value_error()
        # Create a quantum circuit with the guessed angles
        circuit = QuantumCircuit(1)
        circuit.rx(theta_guess, 0)
        circuit.rz(phi_guess, 0)

        # Simulate the circuit and get the resulting state vector
        job = execute(circuit, simulator)
        result = job.result()
        statevector = result.get_statevector(circuit)

        # Check if the guessed state matches the target state
        if np.allclose(target_state, statevector):
            print("Congratulations! Your guess is correct.")
            break
        else:
            print("Incorrect guess.\n")
            A = input("Type restart to restart the game else press enter to exit to main menu")
            if A.upper() == "RESTART":
                guess_quantum_state()
            else:
                time.sleep(2)
                print("Returning to the Main Menu....")
                clear_terminal()
                print_welcome_banner()

simulator = Aer.get_backend('statevector_simulator')

# Function to play the Quantum Coin Flip game
def play_quantum_coin_flip():
    print("A) Heads")
    print("B) Tails")
    l=input("Enter an Option: ")
    # Create a quantum circuit with 1 qubit
    circuit = QuantumCircuit(1, 1)

    # Apply a Hadamard gate to the qubit to put it in a superposition
    circuit.h(0)

    # Measure the qubit
    circuit.measure(0, 0)

    # Simulate the circuit using the local Aer simulator
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator)

    # Get the result of the measurement
    result = job.result()
    counts = result.get_counts(circuit)

    # Extract the outcome from the measurement result
    outcome = list(counts.keys())[0]
    # Determine the outcome based on the measurement result
    if outcome == '0' and l.upper()=="A":
        print("Congratulations! Your Guess was right and it is Heads!")
        print("Do you want to restart the game?Yes or No")
        A = input()
        if A.upper() == "YES":
            clear_terminal()
            print("restarting in 5 second")
            time.sleep(5)
            play_quantum_coin_flip()
        elif A.upper() == "No":
            print_welcome_banner()

    elif outcome == '1' and l.upper()=="B":
        print("Congratulations! Your Guess was right and it is Tails!")
        print("Do you want to restart the game?Yes or No")
        A = input()
        if A.upper() == "YES":
            clear_terminal()
            print("restarting in 5 second")
            time.sleep(5)
            play_quantum_coin_flip()
        elif A.upper() == "No":
            print_welcome_banner()

    else:
        print("Your Guess is Wrong.")
        print("Do you want to restart the game?Yes or No")
        A = input()
        if A.upper() == "YES":
            clear_terminal()
            print("restarting in 5 second")
            time.sleep(5)
            play_quantum_coin_flip()
        elif A.upper() == "NO":
            print_welcome_banner()

def print_welcome_banner():
    time.sleep(2)
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # Customize the content and design of the banner
    banner = f"""
*****************************************************
*                                                   *
*                  Welcome to Quntaum Games         *
*                                                   *
*        Current Date: {current_date}                   *
*        Current Time: {current_time}                     *
*                                                   *
*****************************************************

    """

    print(banner)
    while True:
        display_menu()
        ui = input("Enter a Option: ")
        if ui.upper() == "A":
            clear_terminal()
            print("Game Starting in 5 Second,Good Luck")
            time.sleep(5)
            guess_quantum_state()
            game_over = True
            if game_over:
                input("Press Enter to continue to the main menu")
                game_over = False

        elif ui.upper() == "B":
            clear_terminal()
            print("Game is Starting in 5 Second,Good Luck")
            time.sleep(5)
            play_quantum_coin_flip()


        elif ui.upper() == "X":
            print("Goodbye")
            quit()

        else:
            print("Invalid Option,enter a Correct Option.")
            print_welcome_banner()


# Call the function to print the custom welcome banner with the current date and time
print_welcome_banner()


