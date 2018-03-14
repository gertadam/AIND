# """game_agent.py Gert
# Finish all TODO items in this file to complete the isolation project, then
# test your agent's strength against a set of known agents using tournament.py
# and include the results in your report.
# """
# import random
#
# Verbose = False
#
# class SearchTimeout(Exception):
#     """Subclass base exception for code clarity. """
#     pass
#
#
# def custom_score(game, player):
#     """Calculate the heuristic value of a game state from the point of view
#     of the given player.
#
#     This should be the best heuristic function for your project submission.
#
#     Note: this function should be called from within a Player instance as
#     `self.score()` -- you should not need to call this function directly.
#
#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).
#
#     player : object
#         A player instance in the current game (i.e., an object corresponding to
#         one of the player objects `game.__player_1__` or `game.__player_2__`.)
#
#     Returns
#     -------
#     float
#         The heuristic value of the current game state to the specified player.
#     """
#     x = game.get_legal_moves(player)
#     heu_val=len(x)
#     return heu_val
#
#
# def custom_score_2(game, player):
#     """Calculate the heuristic value of a game state from the point of view
#     of the given player.
#
#     Note: this function should be called from within a Player instance as
#     `self.score()` -- you should not need to call this function directly.
#
#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).
#
#     player : object
#         A player instance in the current game (i.e., an object corresponding to
#         one of the player objects `game.__player_1__` or `game.__player_2__`.)
#
#     Returns
#     -------
#     float
#         The heuristic value of the current game state to the specified player.
#     """
#     x = game.get_legal_moves(player)
#     heu_val=len(x)
#     return heu_val
#
#
# def custom_score_3(game, player):
#     """Calculate the heuristic value of a game state from the point of view
#     of the given player.
#
#     Note: this function should be called from within a Player instance as
#     `self.score()` -- you should not need to call this function directly.
#
#     Parameters
#     ----------
#     game : `isolation.Board`
#         An instance of `isolation.Board` encoding the current state of the
#         game (e.g., player locations and blocked cells).
#
#     player : object
#         A player instance in the current game (i.e., an object corresponding to
#         one of the player objects `game.__player_1__` or `game.__player_2__`.)
#
#     Returns
#     -------
#     float
#         The heuristic value of the current game state to the specified player.
#     """
#     x = game.get_legal_moves(player)
#     heu_val=len(x)
#     return heu_val
#
#
# class IsolationPlayer:
#     """Base class for minimax and alphabeta agents -- this class is never
#     constructed or tested directly.
#
#     ********************  DO NOT MODIFY THIS CLASS  ********************
#
#     Parameters
#     ----------
#     search_depth : int (optional)
#         A strictly positive integer (i.e., 1, 2, 3,...) for the number of
#         layers in the game tree to explore for fixed-depth search. (i.e., a
#         depth of one (1) would only explore the immediate sucessors of the
#         current state.)
#
#     score_fn : callable (optional)
#         A function to use for heuristic evaluation of game states.
#
#     timeout : float (optional)
#         Time remaining (in milliseconds) when search is aborted. Should be a
#         positive value large enough to allow the function to return before the
#         timer expires.
#     """
#     def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
#         self.search_depth = search_depth
#         self.score = score_fn
#         self.time_left = None
#         self.TIMER_THRESHOLD = timeout
#
#
# class MinimaxPlayer(IsolationPlayer):
#     """Game-playing agent that chooses a move using depth-limited minimax
#     search. You must finish and test this player to make sure it properly uses
#     minimax to return a good move before the search time limit expires.
#     """
#
#     def get_move(self, game, time_left):
#         """Search for the best move from the available legal moves and return a
#         result before the time limit expires.
#
#         **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************
#
#         For fixed-depth search, this function simply wraps the call to the
#         minimax method, but this method provides a common interface for all
#         Isolation agents, and you will replace it in the AlphaBetaPlayer with
#         iterative deepening search.
#
#         Parameters
#         ----------
#         game : `isolation.Board`
#             An instance of `isolation.Board` encoding the current state of the
#             game (e.g., player locations and blocked cells).
#
#         time_left : callable
#             A function that returns the number of milliseconds left in the
#             current turn. Returning with any less than 0 ms remaining forfeits
#             the game.
#
#         Returns
#         -------
#         (int, int)
#             Board coordinates corresponding to a legal move; may return
#             (-1, -1) if there are no available legal moves.
#         """
#         self.time_left = time_left
#
#         # Initialize the best move so that this function returns something
#         # in case the search fails due to timeout
#         best_move = (-1, -1)
#
#         try:
#             # The try/except block will automatically catch the exception
#             # raised when the timer is about to expire.
#             return self.minimax(game, self.search_depth)
#
#         except SearchTimeout:
#             pass  # Handle any actions required after timeout as needed
#
#         # Return the best move from the last completed search iteration
#         return best_move
#
#     def minimax(self, game, depth):
#         """Implement depth-limited minimax search algorithm as described in
#         the lectures.
#
#         This should be a modified version of MINIMAX-DECISION in the AIMA text.
#         https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md
#
#         **********************************************************************
#             You MAY add additional methods to this class, or define helper
#                  functions to implement the required functionality.
#         **********************************************************************
#
#         Parameters
#         ----------
#         game : isolation.Board
#             An instance of the Isolation game `Board` class representing the
#             current game state
#
#         depth : int
#             Depth is an integer representing the maximum number of plies to
#             search in the game tree before aborting
#
#         Returns
#         -------
#         (int, int)
#             The board coordinates of the best move found in the current search;
#             (-1, -1) if there are no legal moves
#
#         Notes
#         -----
#             (1) You MUST use the `self.score()` method for board evaluation
#                 to pass the project tests; you cannot call any other evaluation
#                 function directly.
#
#             (2) If you use any helper functions (e.g., as shown in the AIMA
#                 pseudocode) then you must copy the timer check into the top of
#                 each helper function or else your agent will timeout during
#                 testing.
#         """
#         self.time_test()
#         best_score = float("-inf")
#         # Initialize the best move so that this function returns something
#         # in case the search fails due to timeout
#         best_move = (-1, -1)
#         for m in game.get_legal_moves():
#             # call has been updated with a depth limit
#             v = self.min_value(game.forecast_move(m), depth - 1)
#             if v > best_score:
#                 best_score = v
#                 best_move = m
#         return best_move
#
#
#     def min_value(self, gameState, depth):
#         """ Return the value for a win (+1) if the game is over,
#         otherwise return the minimum value over all legal child
#         nodes.
#         """
#         self.time_test()
#
#         if self.terminal_test(gameState):
#             return float("inf")  # by assumption 2
#
#         # New conditional depth limit cutoff
#         v = float("inf")
#         if depth <= 0:  # "==" could be used, but "<=" is safer
#             return self.score(gameState, self)
#         else:
#             for m in gameState.get_legal_moves():
#                 # the depth should be decremented by 1 on each call
#                 v = min(v, self.max_value(gameState.forecast_move(m), depth - 1))
#             return v
#
#
#     def max_value(self, gameState, depth):
#         """ Return the value for a loss (-1) if the game is over,
#         otherwise return the maximum value over all legal child
#         nodes.
#         """
#         self.time_test()
#
#         if self.terminal_test(gameState):
#             return float("inf")  # by assumption 2
#
#         # New conditional depth limit cutoff
#         v = float("-inf")
#         if depth <= 0:  # "==" could be used, but "<=" is safer
#             return self.score(gameState, self)
#         else:
#             for m in gameState.get_legal_moves():
#                 # the depth should be decremented by 1 on each call
#                 v = max(v, self.min_value(gameState.forecast_move(m), depth - 1))
#             return v
#
#     def terminal_test(self, gamestate):
#         moves_available = bool(gamestate.get_legal_moves()) # by Assumption 1
#         return not moves_available
#
#     def time_test(self):
#         if (self.time_left() < self.TIMER_THRESHOLD):
#             if Verbose:
#                 print("Timeout")
#             raise SearchTimeout()
#
# class AlphaBetaPlayer(IsolationPlayer):
#     """Game-playing agent that chooses a move using iterative deepening minimax
#     search with alpha-beta pruning. You must finish and test this player to
#     make sure it returns a good move before the search time limit expires.
#     """
#
#     def get_move(self, game, time_left):
#         """Search for the best move from the available legal moves and return a
#         result before the time limit expires.
#
#         Modify the get_move() method from the MinimaxPlayer class to implement
#         iterative deepening search instead of fixed-depth search.
#
#         **********************************************************************
#         NOTE: If time_left() < 0 when this function returns, the agent will
#               forfeit the game due to timeout. You must return _before_ the
#               timer reaches 0.
#         **********************************************************************
#
#         Parameters
#         ----------
#         game : `isolation.Board`
#             An instance of `isolation.Board` encoding the current state of the
#             game (e.g., player locations and blocked cells).
#
#         time_left : callable
#             A function that returns the number of milliseconds left in the
#             current turn. Returning with any less than 0 ms remaining forfeits
#             the game.
#
#         Returns
#         -------
#         (int, int)
#             Board coordinates corresponding to a legal move; may return
#             (-1, -1) if there are no available legal moves.
#         """
#         self.time_left = time_left
#
#         if len(game.get_legal_moves()) == 0:
#             return (-1, -1)
#
#         # Initialize the best move so that this function returns something
#         # in case the search fails due to timeout
#         best_move = (-1, -1)
#
#         blanks_list = game.get_blank_spaces()
#         #random.shuffle(blanks_list)
#
#         for depth in range(1, len(blanks_list)):
#             try:
#                 best_move = self.alphabeta(game, depth)
#             except SearchTimeout:
#                 return best_move
#         return best_move
#
#
#
#     def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
#         """Implement depth-limited minimax search with alpha-beta pruning as
#         described in the lectures.
#
#         This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
#         https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md
#
#         **********************************************************************
#             You MAY add additional methods to this class, or define helper
#                  functions to implement the required functionality.
#         **********************************************************************
#
#         Parameters
#         ----------
#         game : isolation.Board
#             An instance of the Isolation game `Board` class representing the
#             current game state
#
#         depth : int
#             Depth is an integer representing the maximum number of plies to
#             search in the game tree before aborting
#
#         alpha : float
#             Alpha limits the lower bound of search on minimizing layers
#
#         beta : float
#             Beta limits the upper bound of search on maximizing layers
#
#         Returns
#         -------
#         (int, int)
#             The board coordinates of the best move found in the current search;
#             (-1, -1) if there are no legal moves
#
#         Notes
#         -----
#             (1) You MUST use the `self.score()` method for board evaluation
#                 to pass the project tests; you cannot call any other evaluation
#                 function directly.
#
#             (2) If you use any helper functions (e.g., as shown in the AIMA
#                 pseudocode) then you must copy the timer check into the top of
#                 each helper function or else your agent will timeout during
#                 testing.
#         """
#         self.time_test()
#         best_score = float("-inf")
#         # Initialize the best move so that this function returns something
#         # in case the search fails due to timeout
#         best_move = (-1, -1)
#         for m in game.get_legal_moves():
#             # call has been updated with alpha & beta
#             v = self.max_value(game.forecast_move(m), depth - 1, alpha, beta)
#             if v > best_score:
#                 best_score = v
#                 best_move = m
#             alpha = max(alpha, v)
#         return best_move
#
#
#     def max_value(self, gameState, depth, alpha, beta):
#         """ Return the value for a loss (-1) if the game is over,
#         otherwise return the maximum value over all legal child
#         nodes.
#         """
#         n_moves = len(gameState.get_legal_moves())
#         legal = gameState.get_legal_moves()
#
#         self.time_test()
#
#         if self.terminal_test(gameState):
#             #return gameState.utility(gameState)
#             return float("inf")  # by assumption 2
#
#         # New conditional depth limit cutoff
#         v = float("-inf")
#         if depth == 0:
#             return self.score(gameState, self)
#         # elif (n_moves == 1):
#         #    return max(v, self.min_value(gameState.forecast_move(legal[0]), depth - 1, alpha, beta))
#         # else:
#         for m in legal:
#             # the depth should be decremented by 1 on each call
#             v = max(v, self.min_value(gameState.forecast_move(m), depth - 1, alpha, beta))
#             if (v >= beta):
#                 return v
#             alpha = max(alpha, v)
#         return v
#
#
#     def min_value(self, gameState, depth, alpha, beta):
#         """ Return the value for a win (+1) if the game is over,
#         otherwise return the minimum value over all legal child
#         nodes.
#         """
#         n_moves = len(gameState.get_legal_moves())
#         legal = gameState.get_legal_moves()
#
#         self.time_test()
#
#         if self.terminal_test(gameState):
#             #return gameState.utility(gameState)
#             return float("inf")  # by assumption 2
#
#         # New conditional depth limit cutoff
#         v = float("inf")
#         if depth == 0:
#             return self.score(gameState, self)
#         #elif (n_moves == 1):
#         #    return min(v, self.max_value(gameState.forecast_move(legal[0]), depth - 1, alpha, beta))
#         #else:
#         for m in legal:
#             # the depth should be decremented by 1 on each call
#             v = min(v, self.max_value(gameState.forecast_move(m), depth - 1, alpha, beta))
#             if (v <= alpha):
#                 return v
#             beta = min(beta, v)
#         return v
#
#     def terminal_test(self, gamestate):
#         moves_available = bool(gamestate.get_legal_moves()) # by Assumption 1
#         return not moves_available
#
#     def time_test(self):
#         if (self.time_left() < self.TIMER_THRESHOLD):
#             if Verbose:
#                 print("Timeout")
#             raise SearchTimeout()

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

    p_loc = game.get_player_location(player)
    loc_list1 = game.get_legal_moves()
    blanks_list = game.get_blank_spaces()

    loc_list1.append(p_loc)
    spaces_in_area = []

    for x in loc_list1:
        boxsize = 2
        min_r = x[0]-boxsize
        min_c = x[1]-boxsize
        max_r = x[0]+boxsize
        max_c = x[1]+boxsize

        # blanks in box can be up to 25 - 8 pos moves 8*25 200spaces
        for blank in blanks_list:
            if min_r <= blank[0] <= max_r and min_c <= blank[1] <= max_c:
                spaces_in_area.append(blank)

    if 1 <= p_loc[0] <= 6 and 1 <= p_loc[1] <= 6:
        cl_value = 200
    else:
        cl_value = -200

    # moves can tally up to 8
    oppo_mov = float(len(game.get_legal_moves(game.get_opponent(player))))
    my_moves = len(game.get_legal_moves(player))
    if oppo_mov == 1:
        return float("inf")
    if my_moves == 1:
        return float("-inf")

    if oppo_mov == 2:
        return float("500")
    if my_moves == 2:
        return float("-500")


    in_box = ( len(spaces_in_area)*2 )  #  value     2  - 400
    #                     cl_value         value  (-200) - (200)
    # we subtract oppo_mov so in most cases there will be only a difference of 1-3
    mov_diff = ((my_moves-1.5*oppo_mov)*100)

    return float(in_box+cl_value+mov_diff)




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
    blanks_list = game.get_blank_spaces()
    turn = 63-len(blanks_list)
    turn_effect = turn * 0.1       #

    cur_loc = game.get_player_location(player)
    if 1 <= cur_loc[0] <= 6 and 1 <= cur_loc[1] <= 6:
        cl_value=100
    else:
        cl_value=-100


    in_area      = []
    outside_area = []

    legal_list = game.get_legal_moves()
    for in_out in legal_list:
        if 1 <= in_out[0] <= 6 and 1 <= in_out[1] <= 6:
            in_area.append(in_out)         # could be 1-8
        else:
            outside_area.append(in_out)    # can only be 1-4

    in_val  = len(in_area)*turn_effect            # *  0.1 0.2 0.3 0.4 0.5 0.6
    out_val = len(outside_area)*(2-turn_effect)   # *  1.9 1.8 1.7 1.6 1.5 1.4

    return float(cl_value+in_val+out_val)


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

    oppo_mov = float(len(game.get_legal_moves(game.get_opponent(player))))
    my_moves = float(len(game.get_legal_moves(player)))

    if oppo_mov == 1:
        return float("inf")

    if my_moves == 1:
        return float("-inf")

    if oppo_mov == 2:
        return float("500")

    if my_moves == 2:
        return float("-500")


    return float(my_moves-1.5*oppo_mov)




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

        if self.terminal_test(gameState):
            return float("inf")  # by assumption 2

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

        if self.terminal_test(gameState):
            return float("inf")  # by assumption 2

        # New conditional depth limit cutoff
        v = float("-inf")
        if depth <= 0:  # "==" could be used, but "<=" is safer
            return self.score(gameState, self)
        else:
            for m in gameState.get_legal_moves():
                # the depth should be decremented by 1 on each call
                v = max(v, self.min_value(gameState.forecast_move(m), depth - 1))
            return v

    def terminal_test(self, gamestate):
        moves_available = bool(gamestate.get_legal_moves())  # by Assumption 1
        return not moves_available

    def time_test(self):
        if (self.time_left() < self.TIMER_THRESHOLD):
            if Verbose:
                print("Timeout")
            raise SearchTimeout()


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
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
        best_move = (-1, -1)

        blanks_list = game.get_blank_spaces()
        # random.shuffle(blanks_list)

        for depth in range(1, len(blanks_list)):
            try:
                best_move = self.alphabeta(game, depth)
            except SearchTimeout:
                return best_move
        return best_move

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

        max_branche, move = self.max_value(game, depth, alpha, beta)

        return move
        #
        # best_score = float("-inf")
        # # Initialize the best move so that this function returns something
        # # in case the search fails due to timeout
        # best_move = (-1, -1)
        # for m in game.get_legal_moves():
        #     # call has been updated with alpha & beta
        #     v = self.max_value(game.forecast_move(m), depth - 1, alpha, beta)
        #     if v > best_score:
        #         best_score = v
        #         best_move = m
        #     alpha = max(alpha, v)
        # return best_move

    def max_value(self, gameState, depth, alpha, beta):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        n_moves = len(gameState.get_legal_moves())
        legal = gameState.get_legal_moves()

        self.time_test()

        # New conditional depth limit cutoff
        v = float("-inf")
        move_for_v = (-1, -1)

        if self.terminal_test(gameState):
            # return gameState.utility(gameState)
            return float("inf"), move_for_v  # by assumption 2



        if depth == 0:
            return self.score(gameState, self), move_for_v
        # elif (n_moves == 1):
        #    return max(v, self.min_value(gameState.forecast_move(legal[0]), depth - 1, alpha, beta))
        # else:
        for m in legal:
            # the depth should be decremented by 1 on each call
            min_branche, min_branche_move = self.min_value(gameState.forecast_move(m), depth - 1, alpha, beta)
            if min_branche > v:
                v = min_branche
                move_for_v = m

            if (v >= beta):
                return v, move_for_v
            alpha = max(alpha, v)
        return v, move_for_v

    def min_value(self, gameState, depth, alpha, beta):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        n_moves = len(gameState.get_legal_moves())
        legal = gameState.get_legal_moves()

        self.time_test()

        # New conditional depth limit cutoff
        v = float("inf")
        move_for_v = (-1, -1)

        if self.terminal_test(gameState):
            # return gameState.utility(gameState)
            return float("inf"), move_for_v  # by assumption 2


        if depth == 0:
            return self.score(gameState, self), move_for_v
        # elif (n_moves == 1):
        #    return min(v, self.max_value(gameState.forecast_move(legal[0]), depth - 1, alpha, beta))
        # else:
        for m in legal:
            # the depth should be decremented by 1 on each call
            max_branche, max_branche_move = self.max_value(gameState.forecast_move(m), depth - 1, alpha, beta)

            if max_branche < v:
                v = max_branche
                move_for_v = m

            if (v <= alpha):
                return v, move_for_v
            beta = min(beta, v)
        return v, move_for_v

    def terminal_test(self, gamestate):
        moves_available = bool(gamestate.get_legal_moves())  # by Assumption 1
        return not moves_available

    def time_test(self):
        if (self.time_left() < self.TIMER_THRESHOLD):
            if Verbose:
                print("Timeout")
            raise SearchTimeout()

