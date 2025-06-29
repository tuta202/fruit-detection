import os
import shutil
from pathlib import Path

base_path = Path("datasets")
datasets = ["carrot", "corn", "dragonfruit", "fruit"]
splits = ["train", "valid", "test"]
output_dir = Path("merged_dataset")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def merge_datasets():
    for split in splits:
        for dtype in ["images", "labels"]:
            merged_split_path = output_dir / split / dtype
            ensure_dir(merged_split_path)

    for dataset in datasets:
        for split in splits:
            for dtype in ["images", "labels"]:
                src_path = base_path / dataset / split / dtype
                dst_path = output_dir / split / dtype

                if not src_path.exists():
                    continue

                for file in os.listdir(src_path):
                    src_file = src_path / file
                    # add prefix
                    new_name = f"{dataset}_{file}"
                    dst_file = dst_path / new_name
                    shutil.copy(src_file, dst_file)
                    print(f"Copied: {src_file} -> {dst_file}")

if __name__ == "__main__":
    merge_datasets()
