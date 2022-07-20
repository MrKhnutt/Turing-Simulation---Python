# Turing-Simulation---Python
## Turing machine based off of Wikipedia's formal definition, which you can find by clicking [here](https://en.wikipedia.org/wiki/Turing_machine)

Following Hopcroft & Ullman (1979, p. 148), a (one-tape) Turing machine can be formally defined as a 7-tuple M = ⟨ Q , Γ , b , Σ , δ , q 0 , F ⟩ where...
- Γ is a finite, non-empty set of tape alphabet symbols;
- b ∈ Γ is the blank symbol (the only symbol allowed to occur on the tape infinitely often at any step during the computation);
- Σ ⊆ Γ ∖ { b } is the set of input symbols, that is, the set of symbols allowed to appear in the initial tape contents;
- Q is a finite, non-empty set of states;
- q 0 ∈ Q is the initial state;
- F ⊆ Q is the set of final states or accepting states. The initial tape contents is said to be accepted by M if it eventually halts in a state from F.
- δ : ( Q ∖ F ) × Γ ↛ Q × Γ × { L , R } is a partial function called the transition function, where L is left shift, R is right shift. If δ is not defined on the current state and the current tape symbol, then the machine halts; intuitively, the transition function specifies the next state transited from the current state, which symbol to overwrite the current symbol pointed by the head, and the next head movement.
