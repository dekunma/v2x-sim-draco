# V2X-Sim-draco
A program using [draco](https://github.com/google/draco) to compress and then decompress point cloud data of [V2X-Sim Dataset](https://ai4ce.github.io/V2X-Sim/).  
The program will convert the binary point cloud data (`.pcd.bin`) to `.ply` format; then it uses draco to compress and then decompress the point cloud data, and finally convert it back into `.pcd.bin` format.

## Installation
1. Clone this repo and `cd` into its directory
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Clone draco under current directory:
    ```bash
    git clone https://github.com/google/draco
    ```
4. Build draco:
    ```bash
    cd draco

    mkdir build

    cd build

    cmake ../

    make
    ```


## Usage
```bash
python main.py -s /path/to/V2X-Sim/sweeps/dir
```
The output will be stored in `final_output` by default.

## Scripts
Clean intermediate output (everything except the final `.pcd.bin` output):
```bash
make clean_intermediate
```

Clean all the output:
```bash
make clean
```