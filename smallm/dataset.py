import subprocess
from dataclasses import dataclass
from pathlib import Path

import glog
import yaml


@dataclass
class DatasetConfig:
    dataset_file: Path
    output_directory: Path


def download_file(target_url: str, dataset_directory: Path, file_name: str):
    subprocess.run(["wget", "-nc", target_url, "-O", dataset_directory / file_name])


def download_dataset(cfg: DatasetConfig):
    dataset_directory = cfg.output_directory / "datasets" / cfg.dataset_file.stem
    dataset_directory.mkdir(exist_ok=True, parents=True)
    with open(cfg.dataset_file, "r") as handle:
        dataset = yaml.safe_load(handle)
    for file_name, target_url in dataset.items():
        download_file(target_url, dataset_directory, file_name)
