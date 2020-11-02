import re

class FiniteStateManager:
    """Simple finite-state automaton for dialogue management:
    - each state has a unique identifier and is associated with a system response
    - each edge represents a transition between states, and is associated with a regular expression.
    
    """
    
    def __init__(self):
        self.start_state = None
        self.final_states = []
        self.states = {}
        self.edges = {}
        
    def add_state(self, state_id, system_output, is_start=False, is_final=False):
        """Adds a new state with a unique string identifier and a system output (as a string).
        The flags is_start/is_final indicates whether the state is a start or final state"""
        
        if state_id in self.states:
            raise RuntimeError(state_id + " is already present in the automaton")
            
        self.states[state_id] = system_output
        if is_start:
            self.start_state = state_id
        if is_final:
            self.final_states.append(state_id)
            
    def add_edge(self, from_state_id, to_state_id, regexp):
        """Adds a new edge between two states (which must be present in the automaton). Each
        edge is associated with a regular expression (as a string) that specifies the pattern
        that must be matched (on the user input) in order to traverse the edge.
        
        If the regexp is None, the edge is assumed to be empty and will be automatically traversed."""
        
        if from_state_id not in self.states:
            raise RuntimeError(from_state_id + " not in list of possible states")
        if to_state_id not in self.states:
            raise RuntimeError(to_state_id + " not in list of possible states")
            
        self.edges[from_state_id] = self.edges.get(from_state_id, []) + [(to_state_id, regexp)]
        
    def start_dialogue(self):
        """Starts a new dialogue"""
        
        if self.start_state is None:
            raise RuntimeError("No start state has been defined")
        elif len(self.final_states)==0:
            raise RuntimeError("No final state(s) has been defined")
            
        return Interaction(self)
    
    
    def to_smcat(self):
        """Return the finite-state automaton in the SMCAT text format such that it can be 
        easily rendered on https://state-machine-cat.js.org/"""
        
        state_lines = []
        for state, action in self.states.items():
            state_lines.append("\"[%s]\": \" System: '%s' \""%(state, action))
            
        smcat = ",\n".join(state_lines) + ";\n\n"
        
        if self.start_state:
            smcat += "initial => \"[%s]\";\n"%self.start_state

        edge_lines = []
        for from_state_id, edges_from_state in self.edges.items():
            for to_state_id, regexp in edges_from_state:
                edge_val = ": \"User: '%s'\""%regexp if regexp is not None else ""
                edge_lines.append("\"[%s]\" => \"[%s]\" %s;"%(from_state_id, to_state_id, edge_val))
        smcat += "\n".join(edge_lines) + "\n"
        
        for final_state in self.final_states:
            smcat += "\"[%s]\" => final;\n"%final_state
            
        return smcat
            
    
    
class Interaction:
    """Interaction based on a finite-state automaton. The object comprises the automaton itself
    along with a reference to the current dialogue state.
    
    The finite-state automaton is traversed until a final state is reached. In a given state,
    we look at all edges going out of the current state, and check whether the pattern 
    (regular expression) is matched on the user input. If that is the case, we traverse the 
    edge, update the current dialogue state, and produce the corresponding system output.
    
    Note that the patterns are evaluated in the order of insertion of the edges. This means
    that generic "catch-all" patterns should be inserted last.
    """
    
    def __init__(self, fsm):
        self.fsm = fsm
        self.current_state = self.fsm.start_state
        
        # We produce a system response
        print("System: %s"%self.fsm.states[self.current_state])
        # We traverse subsequent empty edges
        self._traverse_empty()
        
        # We continue the dialogue until we reach a final state
        while self.current_state not in self.fsm.final_states:
            
            # We wait for the user to provide an input
            user_input = input("User:")
            
            # And we react to it by moving through the automaton
            self._react(user_input)
        
        
    def _react(self, user_input):
        """React to a given user input by looking at possible edges to traverse (based on
        whether their patterns are matched or not). If a pattern is matched, traverse the edge,
        update the current dialogue state and produce the response."""
                
        # We loop on each edge (in order)
        for to_state_id, regexp in self.fsm.edges.get(self.current_state,[]):
            
            # We check whether the pattern is satisfied or not
            if re.search(regexp, user_input, flags=re.I):
                
                # If yes, we move to the next state
                self.current_state = to_state_id
                
                # We print the associated system response
                system_output = self.fsm.states[self.current_state]
                print("System: %s"%system_output)
                
                # And we traverse subsequent empty edges
                self._traverse_empty()
                
                return
                
        raise RuntimeError("Could not find valid transition from state %s"%self.current_state)
              
                
    def _traverse_empty(self):
        """Traverse empty edges (that is, edges associated with a None regexp)."""
        
        for to_state_id, regexp in self.fsm.edges.get(self.current_state,[]):
            if regexp is None:
                self.current_state = to_state_id
                system_output = self.fsm.states[self.current_state]
                print("System: %s"%system_output)
                self._traverse_empty()
                

                
# Simple example (adapted from the one in the course slides)
if __name__ == "__main__":  
    
    manager = FiniteStateManager()
    manager.add_state("start", "What do you want?", is_start=True)
    manager.add_state("offer_apples", "OK, here are your apples!")
    manager.add_state("offer_oranges", "OK, her are your oranges!")
    manager.add_state("not_understood", "Sorry, I did not understand")
    manager.add_state("end", "Goodbye!", is_final=True)

    manager.add_edge("start", "offer_apples", r"\bapples?\b")
    manager.add_edge("start", "offer_oranges", r"\boranges?\b")
    manager.add_edge("start", "not_understood", r".+")
    manager.add_edge("not_understood", "start", None)
    manager.add_edge("offer_apples", "end", None)
    manager.add_edge("offer_oranges", "end", None)