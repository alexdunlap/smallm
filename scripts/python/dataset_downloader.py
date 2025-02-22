import argparse
from pathlib import Path

import glog

from smallm.dataset import DatasetConfig, download_dataset

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dataset downloader script.")
    parser.add_argument(
        "--dataset",
        help="Path to a yaml dataset file. See `./datasets/` directory for example dataset files.",
        required=True,
    )
    parser.add_argument("--output", help="Directory to where dataset will be saved.", required=True)
    parser.add_argument("--verbosity", default=0, type=int, help="Verbosity level. Options are: [0, 1].")
    args = parser.parse_args()

    cfg = DatasetConfig(
        dataset_file=Path(args.dataset),
        output_directory=Path(args.output),
    )

    if args.verbosity == 0:
        glog.setLevel("INFO")
    elif args.verbosity == 1:
        glog.setLevel("DEBUG")
    else:
        raise NotImplementedError(
            f"\n\nYou passed in '{args.verbosity}' to the --verbosity argument."
            + " It needs to be one of these two: [0, 1].\n"
        )

    download_dataset(cfg)
