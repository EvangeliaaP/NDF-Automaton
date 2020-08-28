# NDF-Automaton
Implementantion of non-deterministic finite automaton using Python for academic purpose.

## How to run
1. Download the NDF_Machine.py
2. Create a json file with the following format or you could download one of the json files that are already in the repository.
```
 {
  "noStates": number of stastes,
  "originalState": the original state,
  "noFinalStates": number of final states,
  "finalStates": list that contains final states,
  "noTransitions": number of states,
  "transitions": list that contains the transition function and the elements should look like this '101'(first number is the present state, the second is the input , the third one is the next state)
}
```
An example of the format:
```
{
  "noStates": 4,
  "originalState": 1,
  "noFinalStates": 2,
  "finalStates": [4],
  "noTransitions": 8,
  "transitions":["102","101","111","203","213","304","404","414"]
}
```
3. Run the script and write the json file name in the terminal.
## How it works
1. The machine accepts two ways of entering the word :
      * whole word
      * character by character
2. Checks for each letter/character the transition from state to state according to the transition function.
3. The word is accepted, when the last input of letter/character causes the machine to halt in one of the final states

