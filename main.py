from engine import Engine
from agent import Agent
from graph import generate_graphs

def main():
    TOTAL_SIMULATION = 100
    AVERAGE_SIMULATION = 1000

    STARTING_RANGE = 1
    RANGE_INCREMENT = 1000
    
    simulations_list = []
    guesses_list = []
    for i in range(TOTAL_SIMULATION):
        total_guesses = 0
        for j in range(AVERAGE_SIMULATION):
            engine = Engine(STARTING_RANGE)
            engine.generate_number()
            agent = Agent(STARTING_RANGE)
            guesses = 0

            while True:
                guess = agent.generate_guess()
                feedback = engine.try_number(guess)
                guesses += 1
                if feedback == "correct":
                    break
                agent.update(feedback)
            
            total_guesses += guesses
            average_guesses = total_guesses / AVERAGE_SIMULATION
            print(f"[{i+1}/{TOTAL_SIMULATION}]  |  [{j+1}/{AVERAGE_SIMULATION}]")
        simulations_list.append(STARTING_RANGE)
        guesses_list.append(average_guesses)
        STARTING_RANGE += RANGE_INCREMENT

    
    generate_graphs(simulations_list, guesses_list)

if __name__ == "__main__":
    main()