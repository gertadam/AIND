"""game_agent.py Gert
Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random

Verbose = False

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    x = game.get_legal_moves(player)
    heu_val=len(x)
    return heu_val


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    x = game.get_legal_moves(player)
    heu_val=len(x)
    return heu_val


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    x = game.get_legal_moves(player)
    heu_val=len(x)
    return heu_val


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        self.time_test()
        best_score = float("-inf")
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)
        for m in game.get_legal_moves():
            # call has been updated with a depth limit
            v = self.min_value(game.forecast_move(m), depth - 1)
            if v > best_score:
                best_score = v
                best_move = m
        return best_move

    
    def min_value(self, gameState, depth):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        self.time_test()
        util = gameState.utility(gameState.active_player)
        if (util != 0):
            return util  # by assumption 2
        
        # New conditional depth limit cutoff
        v = float("inf")
        if depth <= 0:  # "==" could be used, but "<=" is safer 
            return self.score(gameState, self)
        else:
            for m in gameState.get_legal_moves():
                # the depth should be decremented by 1 on each call
                v = min(v, self.max_value(gameState.forecast_move(m), depth - 1))                
            return v

        
    def max_value(self, gameState, depth):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        self.time_test()
        util = gameState.utility(gameState.active_player)
        if (util != 0):
            return util  # by assumption 2
    
        # New conditional depth limit cutoff
        v = float("-inf")
        if depth <= 0:  # "==" could be used, but "<=" is safer 
            return self.score(gameState, self)
        else:
            for m in gameState.get_legal_moves():
                # the depth should be decremented by 1 on each call
                v = max(v, self.min_value(gameState.forecast_move(m), depth - 1))
            return v

    def time_test(self):
        if (self.time_left() < self.TIMER_THRESHOLD):
            if Verbose:
                print("Timeout")
            raise SearchTimeout()

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.

    def __init__(self, game):
        self.FoundCenter = False
        if game.height % 2 == 0:
            if game.width % 2 == 0:
                self.FoundCenter = True
                self.center_h = game.height % 2
                self.center_w = game.width % 2
                self.center = (self.center_h, self.center_w)
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        if len(game.get_legal_moves()) == 0:
            return (-1, -1)

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (2, 2)
        #if self.FoundCenter :
        #    best_move = self.center

        blanks_list = game.get_blank_spaces()
        # if Verbose: print("before: ", blanks_list)
        random.shuffle(blanks_list)
        # if Verbose: print("after : ", blanks_list)
        
        if game.get_player_location(game.active_player) == None:
            # start the game (1st move)
            if best_move in blanks_list:
                return best_move
            else:
                #opponent_loc = game.get_player_location(game.get_opponent(game.active_player))
                #if self.FoundCenter:
                #    if opponent_loc != None:
                #        mirrormove(opponent_loc)
                # else:
                # pick 1st from randomized blanks
                return blanks_list[0]

        # not start move
        else:
            d_count =""
            for depth in range(1, len(blanks_list)):
                try:
                    d_count += "-"+str(depth)
                    best_move = self.alphabeta(game, depth)
                    if Verbose:
                        print("best at: ", d_count)
                except SearchTimeout:
                    return best_move
        return best_move

    def mirrormove(opponent_loc):
        return (self.center_h-opponent_loc[0]+self.center_h, self.center_w-opponent_loc[1]+self.center_w)

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        self.time_test()
        best_score = float("-inf")
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)
        legal = game.get_legal_moves()
        if len(legal) == 1:
            return legal[0]
        else:
            for m in game.get_legal_moves():
                # call has been updated with alpha & beta
                v = self.min_value(game.forecast_move(m), depth - 1, alpha, beta)
                if v > best_score:
                    best_score = v
                    best_move = m
                alpha = max(alpha, v)
        return best_move

    
    def min_value(self, gameState, depth, alpha, beta):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        n_moves = len(gameState.get_legal_moves())
        legal = gameState.get_legal_moves()

        self.time_test()
        util = gameState.utility(gameState.active_player)
        if (util != 0):
            # if Verbose:
            print("util: ", util)
            return util  # by assumption 2

        # New conditional depth limit cutoff
        v = float("inf")
        if depth <= 0:  # "==" could be used, but "<=" is safer
            return self.score(gameState, self)
        elif (n_moves == 1):
            if Verbose:
                print("legal of 1")
            return min(v, self.max_value(gameState.forecast_move(legal[0]), depth - 1, alpha, beta))
        else:
            for m in legal:
                # the depth should be decremented by 1 on each call
                v = min(v, self.max_value(gameState.forecast_move(m), depth - 1, alpha, beta))
                if(v <= alpha):
                    return v
                beta = min(beta, v)
            return v

        
    def max_value(self, gameState, depth, alpha, beta):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        n_moves = len(gameState.get_legal_moves())
        legal = gameState.get_legal_moves()

        self.time_test()
        util = gameState.utility(gameState.active_player)
        if (util != 0):
            return util  # by assumption 2

        # New conditional depth limit cutoff
        v = float("-inf")
        if depth <= 0:  # "==" could be used, but "<=" is safer
            return self.score(gameState, self)
        elif (n_moves == 1):
            if Verbose:
                print("legal of 1")
            return max(v, self.min_value(gameState.forecast_move(legal[0]), depth - 1, alpha, beta))
        else:
            for m in legal:
                # the depth should be decremented by 1 on each call
                v = max(v, self.min_value(gameState.forecast_move(m), depth - 1, alpha, beta))
                if(v >= beta):
                    return v
                alpha = max(alpha, v)
            return v

    def time_test(self):
        if (self.time_left() < self.TIMER_THRESHOLD):
            if Verbose:
                print("Timeout")
            raise SearchTimeout()
