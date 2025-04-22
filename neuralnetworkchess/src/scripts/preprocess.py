import chess.pgn
import os
import numpy as np
from tqdm import tqdm

def parse_pgn_to_fen(pgn_path, output_path, max_games=100000):
    """
    Parse a PNG file to FEN format and save as compressed .npz file
    """

    png = open(pgn_path)
    fen_pos = []
    moves = []
    games_read = 0

    # Create output file for parsed data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)


    # Read the PGN file
    for i in tqdm(range(max_games), desc="Parsing Chess Games"):
        game = chess.pgn.read_game(png)
        if game is None:
            break

        games_read += 1
        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
            fen_pos.append(board.fen())
            moves.append(move.uci())

    # close file
    png.close()


    output_path = os.path.join(output_path, f"{pgn_path.split('/')[-1].replace('.npz')}-{games_read}.npz")
    np.savez_compressed(output_path, fens=fen_pos, moves=moves)
    

parse_pgn_to_fen(
    pgn_path="neuralnetworkchess/data/raw/lichess_db_standard_rated_2013-01.pgn",
    output_path="neuralnetworkchess/data/processed/"
)