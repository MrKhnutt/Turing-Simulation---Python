
# M = ⟨ Q , Γ , b , Σ , δ , q[0] , F ⟩
#   Q    Finite non empty set of states
#   Γ    Tape of alphabet symbols, the alphabet of the machine
#   b    blank symbol, nothing
#   Σ    the input symbols that are a subset of Γ (The alphabet)
#   δ    is a partial function called the transition function, where L is left shift, R is right shift
#           If δ is not defined on the current state and the current tape symbol, the the machine halts.
#           Specifies the next state from the current state, which symbol to overwrite the current symbol,
#           and the next head movement
#   q[0] the initial state
#   F    the set of final states, or the set of accepting states

class TuringMachine:
    def __init__(self):
        self.states = None
        self.alphabet = None
        self.blank = None
        self.input = None
        self.sigma = None
        self.initial = None
        self.accepting = None

        self.debug = False

    def passTuple(self, turingTuple:tuple):
        #TODO
        pass
    def isSubset(self, a, b):
        for i in a:
            for j in b:
                if i == j:
                    return True
        return False

    def setStates(self, states:tuple):
        if len(states) == 0:
            raise ValueError("length of states must be >0")
        if self.states != None:
            raise ValueError("States variable is already set")
        #check that accepting is a subset of states
        if self.accepting != None and not (self.isSubset(self.accepting, states)):
            raise ValueError("accepting is not a subset of states")
        #set variable and return
        self.states = set(states)
    def setAlphabet(self, alphabet:tuple):
        if self.alphabet != None:
            raise ValueError("States variable is already set")
        #check that input is a subset of alphabet
        if self.input != None and not self.isSubset(self.input, alphabet):
            raise ValueError("input is not a subset of alphabet")
        self.alphabet = set(alphabet)
    def setInfinSym(self, symbol):
        if self.blank != None:
            raise ValueError("Inifinite Symbol is already set")
        #TODO blank symbol should be subset of language
        self.blank = symbol
    def setInput(self, symbols:tuple):
        # if self.input != None:
        #     raise ValueError("Input variable is already set")
        if self.alphabet != None and not self.isSubset(self.alphabet, symbols):
            raise ValueError("Input is not a subset of Alphabet")
        self.input = symbols
    def transitionFunction(self, transition):
        '''
        should be a dict of dict of tuple
        tuple should be in the form [write symbol, move tape ('R', 'L', 'N'), and next state]
        '''
        if self.states == None:
            raise ValueError("States must be set before the Transition Function")
        if self.accepting == None:
            raise ValueError("Accepting must be set before the Transition Function")

        #TODO check validity

        #dict of dict of tuple
        self.sigma = transition
    def initialState(self, state):
        # if self.initial != None:
        #     raise ValueError("Initial State is already set")

        #TODO initial state should be an elem of states
        self.initial = state
    def setAcceptence(self, states:tuple):
        if self.accepting != None:
            raise ValueError("Accepting State is already set")
        if self.states != None and not self.isSubset(self.states, states):
            raise ValueError("Acceptence is not a subset of States")
        self.accepting = states

    def run(self):
        tup = (
                self.states,
                self.alphabet,
                self.blank,
                self.input,
                self.sigma,
                self.initial,
                self.accepting
        )
        if None in tup:
            raise ValueError("Not all elements of turing machine set")

        cursor = self.initial
        tape = list(self.input)
        tapepos = 0
        while cursor not in self.accepting:
            entry = self.sigma[cursor][tape[tapepos]]   #get table entry for that frame
            #write                                      #maybe do SQL or something later
            tape[tapepos] = entry[0]
            #move
            if entry[1] == 'R':
                if tapepos == len(tape)-1:  #right overflow, allocate
                    tape.append(self.blank)
                    tapepos += 1
                else:
                    tapepos += 1
            elif entry[1] == 'L':
                if tapepos == 0:    #left overflow, allocate
                    tape = [self.blank] + tape
                else:
                    tapepos -= 1
            #next state
            cursor = entry[2]
        return (tape[tapepos], (tape, tapepos, cursor))
    def clear(self):
        self.input = None
        self.initial = None
if __name__ == '__main__':
    # Turing(('A', 'B', 'C', 'Halt'), (0, 1), 0, (1), )
    tm = TuringMachine()
    tm.setStates(('A','B','C','HALT'))
    tm.setAlphabet((0,1))
    tm.setInfinSym(0)
    tm.setInput((1,))
    tm.initialState('A')
    tm.setAcceptence(('HALT',))

    sigma = {
        'A':{0:(1,'R','B'), 1:(1,'L','C')},
        'B':{0:(1,'L','A'), 1:(1,'R','B')},
        'C':{0:(1,'L','B'), 1:(1,'R','HALT')}
    }
    tm.transitionFunction(sigma)
    tm.debug = True

    tm.run()
