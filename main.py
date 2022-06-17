import os
import argparse
from utils import convert_bin_pcd_to_ply, convert_ply_to_bin_pcd, draco_compress, draco_decompress

def main(sweeps_dir):
    for d in os.listdir(sweeps_dir):
        if not d.startswith('LIDAR'):
            continue

        from_path = os.path.join(sweeps_dir, d)
        print(from_path)
        for f in os.listdir(from_path):
            if not f.endswith('pcd.bin'):
                continue

            input_file_path = os.path.join(from_path, f)
            ply_file_name = convert_bin_pcd_to_ply(input_file_path)
            draco_compress(ply_file_name, os.path.join('ply_data', d))
            draco_decompress(ply_file_name.split('.')[0] + '.drc', os.path.join('draco_intermediate', d))
            convert_ply_to_bin_pcd(ply_file_name, os.path.join('draco_output', d))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--sweeps_root",
        default='/scratch/dm4524/data/V2X-Sim-2/sweeps',
        type=str,
        help="The path to the sweeps directory of V2X-Sim.",
    )

    args = parser.parse_args()
    main(args.sweeps_root)