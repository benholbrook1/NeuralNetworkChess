chess_ai/
│
├── data/                   # Raw and processed data
│   ├── raw/                # Original PGN files from Lichess
│   ├── processed/          # Processed FEN + move data (e.g., .npz, .h5)
│   └── self_play/          # Self-play generated games (RL phase)
│
├── notebooks/              # Jupyter notebooks for exploration
│   ├── Data_Preprocessing.ipynb
│   └── Model_Prototyping.ipynb
│
├── src/                    # Core Python modules
│   ├── environment/        # Chess game logic
│   │   ├── board.py        # Board state handling (uses python-chess)
│   │   └── game.py         # Game simulation wrapper
│   │
│   ├── models/             # Neural networks
│   │   ├── base_model.py   # Shared ResNet backbone
│   │   ├── policy_head.py  # Move probabilities
│   │   └── value_head.py   # Position evaluation
│   │
│   ├── rl/                 # Reinforcement learning
│   │   ├── mcts.py         # Monte Carlo Tree Search
│   │   └── trainer.py      # Self-play + RL training loop
│   │
│   ├── utils/              # Helper functions
│   │   ├── data_loader.py  # Load PGN/FEN data
│   │   ├── config.py       # Hyperparameters (LR, batch size)
│   │   └── logger.py       # WandB/TensorBoard logging
│   │
│   └── scripts/            # One-off utility scripts
│       ├── preprocess.py   # Convert PGN to FEN
│       └── evaluate.py     # Test AI vs. Stockfish
│
├── saved_models/           # Trained model checkpoints
│   ├── supervised/         # Pretrained weights
│   └── rl/                # RL-trained weights
│
├── tests/                  # Unit tests
│   ├── test_board.py
│   └── test_mcts.py
│
├── requirements.txt        # Python dependencies
├── config.yaml             # Centralized hyperparameters
└── README.md               # Project overview + setup instructions